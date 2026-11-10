# motor.py
import time
import RPi.GPIO as GPIO  # Raspberry Pi 5 : fournir cette API avec le paquet système python3-rpi-lgpio.

class StepperMotor:
    def __init__(self, step_pin, dir_pin, en_pin):
        """Initialise une instance de moteur pas-à-pas sur Raspberry Pi 5."""
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        self.en_pin = en_pin

        # Utilisation de la numérotation BCM des broches (GPIO 12, 13, 5, 6, 23)
        GPIO.setmode(GPIO.BCM)  # Sert à la biblio pour savoir comment interpréter les numéros. voir config.py
        GPIO.setwarnings(False) # n'envoie plus d'avertissement.

        # Configuration des broches STEP et DIR en SORTIE et mise à 0 par sécurité
        GPIO.setup(self.step_pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.dir_pin, GPIO.OUT, initial=GPIO.LOW)

        # Configuration de la broche EN en SORTIE (HIGH = moteur désactivé/libre par défaut)
        GPIO.setup(self.en_pin, GPIO.OUT, initial=GPIO.HIGH)

    def enable(self):
        """Active le driver TMC2209 (Active LOW) : verrouille l'axe avec le couple de maintien."""
        GPIO.output(self.en_pin, GPIO.LOW)

    def disable(self):
        """Désactive le driver TMC2209 (HIGH) : libère l'axe pour un déplacement manuel."""
        GPIO.output(self.en_pin, GPIO.HIGH)

    def set_direction(self, forward=True):
        """Définit le sens de rotation du moteur. Pour savoir si c'est dans le sens de l'augmentation de RA ou DEC."""
        GPIO.output(self.dir_pin, GPIO.HIGH if forward else GPIO.LOW)

    def pulse(self, half_period_s):
        """Génère une impulsion carrée (50% duty cycle) sur la broche STEP."""
        GPIO.output(self.step_pin, GPIO.HIGH)
        time.sleep(half_period_s)
        GPIO.output(self.step_pin, GPIO.LOW)
        time.sleep(half_period_s)

# fait