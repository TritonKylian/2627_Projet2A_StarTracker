# ephemeris.py
import ephem
import math

class EphemerisCalculator:
    """
    Classe utilitaire pour calculer les coordonnées équatoriales (RA/DEC) 
    d'un astre en temps réel en fonction de la position exacte de l'observateur.
    """
    def __init__(self, lat: float, lon: float, elevation: float = 0):
        # Configuration statique de l'observateur
        self.observer = ephem.Observer()
        # PyEphem attend des chaînes de caractères pour les degrés (ex: '49.0333')
        self.observer.lat = str(lat)       
        self.observer.lon = str(lon)
        self.observer.elevation = float(elevation)
        
        # Dictionnaire des objets du système solaire (Calculs orbitaux complexes)
        self.solar_system = {
            "Soleil": ephem.Sun, 
            "Lune": ephem.Moon, 
            "Mercure": ephem.Mercury,
            "Venus": ephem.Venus, 
            "Mars": ephem.Mars, 
            "Jupiter": ephem.Jupiter,
            "Saturne": ephem.Saturn, 
            "Uranus": ephem.Uranus, 
            "Neptune": ephem.Neptune
        }

    def get_coordinates(self, target_name: str):
        """
        Calcule la position apparente de la cible à l'instant T.
        Retourne un tuple (ra_en_heures, dec_en_degres).
        """
        # Mise à jour de l'heure exacte à l'instant de la requête
        # Assurez-vous que l'horloge système du Raspberry Pi est synchronisée !
        self.observer.date = ephem.now()   

        # Identification et instanciation de l'astre
        # On vérifie d'abord si c'est une planète/lune/soleil
        if target_name in self.solar_system:
            target = self.solar_system[target_name]()
        else:
            try:
                # Recherche dans le catalogue d'étoiles fixes intégré (ex: "Sirius", "Vega")
                # Attention : PyEphem attend le nom international (en anglais)
                target = ephem.star(target_name)
            except KeyError:
                raise ValueError(f"Erreur : L'astre '{target_name}' n'est pas reconnu. "
                                 f"Vérifiez l'orthographe (utilisez l'anglais pour les étoiles).")

        # Calcul de la position apparente depuis votre position sur Terre
        target.compute(self.observer)

        # Conversion des résultats bruts (Radians) en formats standards (Heures et Degrés)
        # PyEphem renvoie l'Ascension Droite en radians. (2*PI radians = 24h)
        ra_hours = target.ra * 12.0 / math.pi
        
        # PyEphem renvoie la Déclinaison en radians. (2*PI radians = 360°)
        dec_degrees = target.dec * 180.0 / math.pi

        return ra_hours, dec_degrees


# TEST indépendant de la classe ci dessus.
if __name__ == "__main__":
    print("--- Test de l'intelligence astronomique (POC) ---")
    
    # Simulation de vos coordonnées géographiques (Exemple : ENSEA, Cergy, France)
    # N'hésitez pas à les modifier avec vos coordonnées exactes.
    LATITUDE_ENSEA = 49.0333
    LONGITUDE_ENSEA = 2.0667
    ALTITUDE_ENSEA = 45.0
    
    try:
        # Instanciation de notre calculateur pour Cergy
        calc = EphemerisCalculator(LATITUDE_ENSEA, LONGITUDE_ENSEA, ALTITUDE_ENSEA)
        
        # Test 1 : Un objet mouvant du système solaire
        cible_1 = "Saturne"
        ra_1, dec_1 = calc.get_coordinates(cible_1)
        print(f"\n[SUCCÈS] Coordonnées de {cible_1} :")
        print(f"-> RA : {ra_1:.4f} h")
        print(f"-> DEC: {dec_1:.4f} °")

        # Test 2 : Une étoile fixe
        cible_2 = "Sirius"
        ra_2, dec_2 = calc.get_coordinates(cible_2)
        print(f"\n[SUCCÈS] Coordonnées de {cible_2} :")
        print(f"-> RA : {ra_2:.4f} h")
        print(f"-> DEC: {dec_2:.4f} °")
        
    except ValueError as e:
        print(e)