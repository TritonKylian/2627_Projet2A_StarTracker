# **Notes par séance**

# Séance 1 15/09

lien utile : https://wiki.openastrotech.com/OpenAstroTracker?fbclid=PARlRTSASfdwVleHRuA2FlbQIxMABzcnRjBmFwcF9pZA8xMjQwMjQ1NzQyODc0MTQAAadvZ97G8UxoVBNb6yF2YV2TA-p9tFaySTwUSeoviNoFVP3lmXYda9JuVb-8XQ\_aem\_y930qqPCMkbocdRs-umUJw


 **Cahier des charges** 
 *Fonctions principales*
- stabiliser l'appareil photo
- repérer et suivre les étoiles ou constellations


**notes discussion avecc les profs**
pas de traitement d'image

juste tracking

3 axes de roation donc 3 moteurs, bien démultipliés pour être précis (X200 par ex, on veut environ 1milidegré)

asservissement en position et inclinatison (moteurs pas à pas et driver de moteur)

moteur puissant pour tenir les 3-4Kg de l'appareil

connexion internet pour recuperer une base de données d'étaoiles (utiliser une rasberry)

recuperer la position et l'incclinison ( accéléromettrre)

**si on a le temps** :
recuperer la photo avec un cable usb

## objectifs :
- faire la base méca surtout : recupere les bases sur intenret
- plus important  c'est l'elec donc on est rapide et efficace sur la méca  
- determiner quel couple/viteesse et precision on veut

## Schéma global du système

<img width="1267" height="392" alt="Diagramme sans nom-Page-3 drawio (1)" src="https://github.com/user-attachments/assets/4a521e9e-51be-4dd7-802b-591467908376" />


## Tâches :
  ### Mécanique et automatique
1- determiner la poids de l'appareil + téléobjectif

2- déterminer puissance/couple/vitesse/précision nécessaire (à noter dans le cahier des charges)

3- choisir des moteurs

### Electronique
- choisir des drivers
- choisir l'accéléromètre

### Software
- choisir la rasberry
- trouver la base de donnée optimale
- trouver quel interface utiliser
- trouver comment déterminer la position voulue
- trouver comment commander les moteurs pour avoir la bonne position



