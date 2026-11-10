# worker.py
import json
import redis
from rq import SimpleWorker, Queue
from controller import Controller
from ephemeris import EphemerisCalculator

# Connexion à Redis
listen = ['high', 'default', 'low']
conn = redis.from_url('redis://localhost:6379')
POSITION_KEY = 'oat:mount_position'

# Constantes de l'observateur (Exemple : Cergy)
LAT = 49.0333
LON = 2.0667
ALT = 45.0

# Instance unique persistante dans le processus du Worker pour maintenir le PWM RPi.GPIO actif
_oat_instance = None

def get_oat() -> Controller:
    global _oat_instance
    if _oat_instance is None:
        _oat_instance = Controller()
    return _oat_instance


def _coordinates_for(target_name: str):
    calc = EphemerisCalculator(LAT, LON, ALT)
    return calc.get_coordinates(target_name)


def stop_mount_tracking():
    """Arrête le suivi et libère les moteurs (EN = HIGH) pour le déplacement manuel."""
    oat = get_oat()
    try:
        oat.disable_motors()
        oat.current_ra_h = None
        oat.current_dec_d = None
    finally:
        conn.delete(POSITION_KEY)
    return "Suivi sidéral arrêté et moteurs libérés pour l'alignement manuel."


def align_mount_to_target(reference_name: str):
    """Verrouille les moteurs (EN = LOW), enregistre l'astre centré manuellement et lance le suivi."""
    reference_ra, reference_dec = _coordinates_for(reference_name)
    oat = get_oat()
    try:
        oat.stop_sidereal_tracking()
        oat.align_to(reference_ra, reference_dec)
        conn.set(POSITION_KEY, json.dumps({
            'ra_h': reference_ra,
            'dec_d': reference_dec,
        }))
        oat.start_sidereal_tracking()
        return (
            f"Monture alignée sur {reference_name} "
            f"(RA {reference_ra:.4f} h, DEC {reference_dec:.4f}°), moteurs verrouillés et suivi activé."
        )
    except Exception:
        conn.delete(POSITION_KEY)
        oat.stop_sidereal_tracking()
        raise


def move_mount_to_target(target_name: str):
    """Pointe vers une cible depuis la dernière position validée et reprend le suivi."""
    print(f"[WORKER] Démarrage de la tâche pour la cible : {target_name}")
    target_ra, target_dec = _coordinates_for(target_name)
    serialized_position = conn.get(POSITION_KEY)
    if serialized_position is None:
        raise RuntimeError(
            "Monture non alignée : arrêtez le suivi, centrez un astre connu, "
            "puis envoyez une demande d'alignement."
        )

    try:
        position = json.loads(serialized_position)
        current_ra = position['ra_h']
        current_dec = position['dec_d']
    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        conn.delete(POSITION_KEY)
        raise RuntimeError("Position mémorisée invalide ; un nouvel alignement est nécessaire.") from exc

    print(f"[WORKER] {target_name} trouvé à RA: {target_ra:.4f}h, DEC: {target_dec:.4f}°")
    oat = get_oat()
    try:
        oat.align_to(current_ra, current_dec)
        oat.stop_sidereal_tracking()
        oat.goto_target(target_ra, target_dec)
        conn.set(POSITION_KEY, json.dumps({
            'ra_h': target_ra,
            'dec_d': target_dec,
        }))
        oat.start_sidereal_tracking()
        return f"Succès : Monture pointée sur {target_name} et en suivi."
    except Exception:
        conn.delete(POSITION_KEY)
        oat.stop_sidereal_tracking()
        raise


if __name__ == '__main__':
    # Les pas peuvent avoir été perdus hors tension ou lors d'un déplacement manuel.
    conn.delete(POSITION_KEY)
    queues = [Queue(name, connection=conn) for name in listen]
    
    # SimpleWorker exécute les jobs dans le processus principal pour conserver le thread PWM actif
    worker = SimpleWorker(queues, connection=conn)
    print("Worker prêt et en écoute sur Raspberry Pi 5...")
    try:
        worker.work()
    finally:
        if _oat_instance is not None:
            _oat_instance.cleanup()