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

<img width="1267" height="402" alt="Diagramme sans nom-Page-3 drawio" src="https://github.com/user-attachments/assets/014a35a7-e178-40b4-bf10-874cd60f2143" />

