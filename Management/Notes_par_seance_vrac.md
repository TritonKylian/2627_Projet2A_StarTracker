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

<img width="1299" height="452" alt="image" src="https://github.com/user-attachments/assets/7acd2e61-1e72-464c-9d06-b2ace2dbbab9" />


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

# Séance 2 22/09
présentation
lien slide : https://docs.google.com/presentation/d/1jDtzcRe_vpuc2h7Jv-1z3r2-y8FQ_S0EBHMQRIcyUqQ/edit?hl=fr&slide=id.g3fbd56af096_0_0#slide=id.g3fbd56af096_0_0

### commentaires des profs : 
- enlever le microcontrolleur car pas besoin d'être aussi précis, la rasberry peut envoyer les PWM aux driver directement.
Explications : oui avec la rasberry on va avoir un "djiter" (jsp comment ça s'écrit) sur les PWM (une imprécisiion sur les fronts montants) mais on veut bouger nos moteurs à une fréquenc etellemnt lente que ça changera rien. 

- l'interface sur téléphone peut être une page web implémentée sur la rasberry
  
*Nouveau diagramme* :
<img width="1076" height="459" alt="image" src="https://github.com/user-attachments/assets/eb51de5c-801e-4fdb-a209-888a6ac2000d" />




