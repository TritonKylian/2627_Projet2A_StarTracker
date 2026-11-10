# controller.py
import time
import math
import numbers
import RPi.GPIO as GPIO  # Raspberry Pi 5 : fournir cette API avec le paquet système python3-rpi-lgpio.
from config import CONFIG
from motor import StepperMotor

class Controller:
    def __init__(self):
        # Instanciation directe des deux objets moteurs avec leur broche EN
        self.motor_ra = StepperMotor(
            CONFIG["PIN_RA_STEP"],
            CONFIG["PIN_RA_DIR"],
            CONFIG["PIN_RA_EN"]
        )
        self.motor_dec = StepperMotor(
            CONFIG["PIN_DEC_STEP"],
            CONFIG["PIN_DEC_DIR"],
            CONFIG["PIN_DEC_EN"]
        )

        # Calcul des résolutions mécaniques globales (les pas totaux pour 360°)
        self.ra_steps_per_360 = int(CONFIG["STEPS_PER_REV"] * CONFIG["MICROSTEPPING"] * CONFIG["GEAR_RATIO_RA"])
        self.dec_steps_per_360 = int(CONFIG["STEPS_PER_REV"] * CONFIG["MICROSTEPPING"] * CONFIG["GEAR_RATIO_DEC"])
        
        self.current_ra_h = None    # en heures
        self.current_dec_d = None  # en degré
        self.tracking = False # indique si le suivi sidéral est actif
        self.ra_pwm = None     # contient l'objet PWM pour le suivi sidéral (RA)
        self.motors_enabled = False # indique si les moteurs sont verrouillés (EN = LOW) ou libres (EN = HIGH)

    def enable_motors(self):
        """Active le couple de maintien sur les axes RA et DEC (EN = LOW)."""
        self.motor_ra.enable()
        self.motor_dec.enable()
        if not self.motors_enabled:
            # On attend un court instant pour que les drivers TMC2209 prennent le relais et verrouillent mécaniquement les axes.
            time.sleep(0.01)
        self.motors_enabled = True
        print("Moteurs verrouillés (EN = LOW) : couple de maintien actif.")

    def disable_motors(self):
        """Libère mécaniquement les axes RA et DEC (EN = HIGH) pour l'alignement manuel."""
        self.stop_sidereal_tracking()
        self.motor_ra.disable()
        self.motor_dec.disable()
        self.motors_enabled = False
        print("Moteurs libérés (EN = HIGH) : vous pouvez déplacer la monture manuellement.")

    def start_sidereal_tracking(self):
        """Active le suivi sidéral en tâche de fond avec une fréquence flottante exacte."""
        self._require_alignment()
        self.enable_motors()
        tracking_freq_hz = self.ra_steps_per_360 / CONFIG["SIDEREAL_DAY_S"]
        
        if self.ra_pwm is None:
            self.ra_pwm = GPIO.PWM(self.motor_ra.step_pin, tracking_freq_hz)
        else:
            self.ra_pwm.ChangeFrequency(tracking_freq_hz)
            
        # Rapport cyclique à 50% (échelle de 0 à 100 dans RPi.GPIO)
        self.ra_pwm.start(50.0)
        self.tracking = True
        print(f"Suivi sidéral activé à {tracking_freq_hz:.4f} Hz sur GPIO {self.motor_ra.step_pin}")

    def stop_sidereal_tracking(self):
        """Coupe le signal PWM de suivi sidéral sans relâcher le couple des moteurs."""
        if self.ra_pwm is not None:
            self.ra_pwm.stop()
        GPIO.output(self.motor_ra.step_pin, GPIO.LOW)
        self.tracking = False
        print("Suivi sidéral arrêté.")

    def align_to(self, ra_h, dec_d):
        """Déclare les coordonnées célestes de la cible centrée manuellement et verrouille les axes."""
        self._validate_coordinates(ra_h, dec_d)
        self.enable_motors()
        self.current_ra_h = float(ra_h)
        self.current_dec_d = float(dec_d)

    def goto_target(self, target_ra_h, target_dec_d):
        """Calcule et exécute la cinématique inverse pour le pointage (GoTo)."""
        self._require_alignment()
        self._validate_coordinates(target_ra_h, target_dec_d)

        # Calcul du chemin le plus court sur 24h (évite de faire un tour complet entre 23h et 1h)
        delta_ra_h = (target_ra_h - self.current_ra_h + 12.0) % 24.0 - 12.0
        delta_ra_deg = delta_ra_h * 15.0
        delta_dec_deg = target_dec_d - self.current_dec_d

        steps_ra = int((delta_ra_deg / 360.0) * self.ra_steps_per_360)
        steps_dec = int((delta_dec_deg / 360.0) * self.dec_steps_per_360)

        print(f"GoTo: Déplacement RA = {steps_ra} pas, DEC = {steps_dec} pas")

        if self.tracking:
            self.stop_sidereal_tracking()

        # On s'assure que les moteurs restent verrouillés pendant tout le déplacement
        self.enable_motors()
            
        self._execute_trapezoidal_profile(self.motor_ra, steps_ra)
        self._execute_trapezoidal_profile(self.motor_dec, steps_dec)
        
        self.current_ra_h = float(target_ra_h)
        self.current_dec_d = float(target_dec_d)

    def _require_alignment(self):
        if self.current_ra_h is None or self.current_dec_d is None:
            raise RuntimeError(
                "Monture non alignée. Centrez manuellement un astre connu et appelez align_to() avant le GoTo ou le suivi."
            )

    @staticmethod
    def _validate_coordinates(ra_h, dec_d):
        if (
            not isinstance(ra_h, numbers.Real)
            or not isinstance(dec_d, numbers.Real)
            or not math.isfinite(ra_h)
            or not math.isfinite(dec_d)
            or not 0.0 <= ra_h < 24.0
            or not -90.0 <= dec_d <= 90.0
        ):
            raise ValueError("Coordonnées invalides : RA doit être dans [0, 24[ h et DEC dans [-90, 90]°.")

    def _execute_trapezoidal_profile(self, motor, total_steps):
        """Génère et exécute directement un profil de vitesse trapézoïdal."""
        if total_steps == 0:
            return

        motor.set_direction(total_steps > 0)
        total_steps = abs(total_steps)

        time_to_max = CONFIG["MAX_SPEED_HZ"] / CONFIG["ACCEL_RATE"]
        steps_to_accel = int(0.5 * CONFIG["ACCEL_RATE"] * (time_to_max ** 2))

        if 2 * steps_to_accel > total_steps:
            steps_to_accel = total_steps // 2
            steps_coast = 0
        else:
            steps_coast = total_steps - (2 * steps_to_accel)

        for step in range(total_steps):
            if step < steps_to_accel:
                current_speed = math.sqrt(2 * CONFIG["ACCEL_RATE"] * step) if step > 0 else 10.0
            elif step < steps_to_accel + steps_coast:
                current_speed = float(CONFIG["MAX_SPEED_HZ"])
            else:
                steps_left = total_steps - step
                current_speed = math.sqrt(2 * CONFIG["ACCEL_RATE"] * steps_left)

            current_speed = max(current_speed, 10.0)
            half_period_s = (1.0 / current_speed) / 2.0

            # Envoi direct de l'impulsion au moteur
            motor.pulse(half_period_s)

    def cleanup(self):
        """Désactive les moteurs et libère complètement les GPIO à la fermeture du programme."""
        self.disable_motors()
        self.ra_pwm = None
        GPIO.cleanup()