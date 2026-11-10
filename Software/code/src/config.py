# config.py

CONFIG = {
    # Constantes Astronomiques
    "SIDEREAL_DAY_S": 86164.0905,  # Durée exacte d'une rotation terrestre en secondes
    
    # Configuration Moteurs (NEMA17 + TMC2209)
    "STEPS_PER_REV": 400,          # NEMA17 haute résolution (0.9° par pas entier)
    "MICROSTEPPING": 64,           # TMC2209 (1/64 interpolé vers 1/256 via MicroPlyer jsp trop comment Microplyer fait ça)
    
    # Ratios de réduction mécanique (Courroies + Engrenages)
    "GEAR_RATIO_RA": 400.0 / 16.0, # Couronne 400 dents / Pignon 16 dents
    "GEAR_RATIO_DEC": 400.0 / 16.0, # Same
    
    # Broches GPIO (Notation BCM - Pi 5)
    "PIN_RA_STEP": 12,             # Sortie STEP avec PWM logiciel pour le suivi sidéral
    "PIN_RA_DIR": 6,
    "PIN_RA_EN": 23,               # Broche Enable RA (LOW = bloqué, HIGH = libre)
    "PIN_DEC_STEP": 13,
    "PIN_DEC_DIR": 5,
    "PIN_DEC_EN": 23,              # Broche Enable DEC (Peut partager le GPIO 23 ou utiliser ex: 24)
    
    # Paramètres Cinématiques (GoTo)
    "MAX_SPEED_HZ": 2000,          # Limite de vitesse moteur en pas/seconde / voir plus tard pour mettre des valeurs logique
    "ACCEL_RATE": 500              # Limite d'accélération en pas/seconde^2
}

# Fait