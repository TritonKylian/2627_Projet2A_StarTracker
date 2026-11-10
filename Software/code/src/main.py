# main.py
from controller import Controller
from ephemeris import EphemerisCalculator

def main():
    print("--- Démarrage du StarTracker ---")
    
    # Initialisation (Ex: Cergy)
    calc = EphemerisCalculator(lat=49.0333, lon=2.0667, elevation=45.0)
    oat = Controller()
    
    try:
        # Libère les moteurs (EN = HIGH) pour permettre à l'utilisateur de tourner la monture à la main
        oat.disable_motors()
        
        # La monture doit être centrée manuellement sur cet astre avant validation.
        reference = input("Centrez manuellement un astre connu puis entrez son nom : ").strip()
        reference_ra, reference_dec = calc.get_coordinates(reference)
        
        # align_to() verrouille automatiquement les moteurs (EN = LOW) et enregistre la position
        oat.align_to(reference_ra, reference_dec)
        
        cible = input("Nom de la cible à pointer : ").strip()
        target_ra, target_dec = calc.get_coordinates(cible)
        
        oat.goto_target(target_ra_h=target_ra, target_dec_d=target_dec)
        oat.start_sidereal_tracking()
        
        # Maintient le programme actif pour ne pas couper le PWM immédiatement dans le bloc finally
        input("\nSuivi sidéral en cours. Appuyez sur Entrée (ou Ctrl+C) pour arrêter la monture...\n")
        
    except KeyboardInterrupt:
        print("\nInterruption par l'utilisateur.")
    except Exception as e:
        print(f"Erreur globale: {e}")
    finally:
        oat.cleanup()
        print("Monture arrêtée et broches GPIO libérées.")

if __name__ == "__main__":
    main()