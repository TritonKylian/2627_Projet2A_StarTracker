
**Choix de la Raspberry Pi**

* **Raspberry Pi 4 (2 Go ou 4 Go) / Raspberry Pi 5 :** Choix recommandé. Le calcul de la position des astres et la gestion de la base de données nécessitent un processeur à l'aise avec Python.
* **Raspberry Pi Zero 2 W :** Possible pour réduire la consommation électrique sur batterie, mais la compilation de certaines bibliothèques d'astronomie et la réactivité du serveur web seront plus lentes.

---

**Architecture de l'interface utilisateur**

La méthode la plus simple sans développer d'application mobile native (iOS/Android) consiste à héberger un **serveur Web (Web App)** sur la Raspberry Pi. Le téléphone se connecte au Wi-Fi généré par la Pi (mode Point d'Accès) et ouvre l'interface dans un navigateur.

1. **Backend (Raspberry Pi):** Python / Flask or FastAPII.
Créez un serveur HTTP en Python (Flask ou FastAPI). Il gère la communication avec la base de données d'étoiles, la lecture I2C/SPI de l'accéléromètre et l'envoi des commandes de vitesse/position aux drivers moteurs via les broches GPIO.


2. **Frontend (Téléphone):** HTML / CSS / JavaScript.
Concevez une page web réactive (HTML/JS avec Fetch API ou WebSockets). L'utilisateur sélectionne l'astre désiré dans une liste ou une recherche, puis envoie la consigne au backend.


3. **Point d'accès Wi-Fi:** Configuration Hostapd.
Configurez la Raspberry Pi en point d'accès Wi-Fi autonome (`hostapd` / `dnsmasq`) pour pouvoir connecter le téléphone directement sur le terrain, sans avoir besoin d'un routeur externe.

Attention à la gestion du temps réel pour 3 moteurs pas à pas
Le système d'exploitation Raspberry Pi OS n'est pas un système temps réel (RTOS). Générer des impulsions PWM/Step directement depuis Linux pour 3 moteurs pas à pas simultanément peut provoquer des micro-saccades qui flouteront la prise de vue. Il est fortement recommandé d'ajouter un microcontrôleur intermédiaire (ex: Arduino Nano ou Raspberry Pi Pico) connecté en USB/Série à la Pi principal pour piloter les drivers de moteurs de manière fluide.


