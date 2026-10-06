# **Notes prises à chaque séance**
(par secrétaire Emilie)
# Séance 1 15/09

lien utile : https://wiki.openastrotech.com/OpenAstroTracker?fbclid=PARlRTSASfdwVleHRuA2FlbQIxMABzcnRjBmFwcF9pZA8xMjQwMjQ1NzQyODc0MTQAAadvZ97G8UxoVBNb6yF2YV2TA-p9tFaySTwUSeoviNoFVP3lmXYda9JuVb-8XQ\_aem\_y930qqPCMkbocdRs-umUJw


 **Cahier des charges** 
 *Fonctions principales*
- stabiliser l'appareil photo
- repérer et suivre les étoiles ou constellations


**Notes discussion avecc les profs**
Pas de traitement d'image seulement le tracking photographique.

3 axes de rotation donc 3 moteurs, bien démultipliés pour être précis (X200 par ex, on veut environ 1milidegré donc environ 3.6 secondes d'arc.)

Asservissement en position et inclinatison (moteurs pas à pas et driver de moteur) voir partie Mécanique pour le détail des composants

Moteur capable de tenir les 3-4Kg de l'appareil

connexion internet pour récupérer une base de données d'étoiles (utiliser une rasberry)

récupérer la position et l'inclination ( accéléromètre)

**Si on a le temps** :
récupérer la photo avec un cable usb

## objectifs :
- faire la base mécanique surtout : récupérer les bases sur internet
- plus important  c'est l'éléctronique donc on est rapide et efficace sur la mécanique pour pouvoir se concentrer sur l'électronique et le software.  
- déterminer quel couple/vitesse et précision on veut

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
Explications : oui avec la rasberry on va avoir un "jitter" sur les PWM (une imprécision sur les fronts montants) mais on veut bouger nos moteurs à une fréquence très lente que ça ne changera rien. 

- l'interface sur téléphone peut être une page web implémentée sur la Raspberry. On peut utiliser un framework web pour ça (ex : flask).
  
*Nouveau diagramme* :
<img width="1076" height="459" alt="image" src="https://github.com/user-attachments/assets/eb51de5c-801e-4fdb-a209-888a6ac2000d" />

## pour la prochaine fois
-> savoir qu'est ce qu'on commande et comment pour la méca et elec => Matéo + Athénaïs 

-> prendre en main la rasberry et determiner comment lui faire réaliser ses tâches  => Emilie

-> Calcul de suivi sidéral + calcul de rotation des moteur pour orienter l'appareil photo => Kylian


# Séance 4 6/10
commentaires des profs pendant la soutenance :
- faire l'app web avec django/javascript et python plutot que html (IA autorisées seulement si on comprend ce qu'elle fait)
- les vis et moteurs : chercher dans les tiroirs de la salle de ppz
- revue de schematic avec les profs à la prochaine séance
