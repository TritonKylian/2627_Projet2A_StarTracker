Aide-mémoire

Linux Terminal Cheat Sheets - Commandes de Base

Utiliser les pages de manuel

man command\_name

Afficher les fichiers

Liste les fichiers du répétoire courant :

ls

Liste détaillée :



ls -l

Inclut les fichiers cachés :



ls -a

Naviguer dans les répertoires

cd /path/to/directory

Revenir au répertoire parent :



cd ..

Aller dans le répertoire personnel :



cd \~

Afficher le chemin actuel

pwd

Créer un répertoire

Crée un répertoire :

mkdir directory\_name

Crée les répertoires parents si nécessaire :



mkdir -p /path/to/directory

Supprimer des fichiers et des répertoires

rm file\_name

Supprimer un répertoire et son contenu :



rm -r directory\_name

Forcer la suppression sans demander confirmation :



rm -f file\_name

Que fait ce code ? (ne pas le faire !)

sudo rm -rf /

sudo rm -rf /: The Command You Should Never Run

Copier des fichiers et des répertoires

cp source\_file destination\_file

cp -r source\_directory destination\_directory

Déplacer/renommer des fichiers et des répertoires

mv source destination

Affichage et Manipulation de Fichiers

Affichage du fichier dans la console :

cat file\_name

Affichage page par page :



less file\_name

Autre affichage page par page :



more file\_name

Éditer un fichier

Ouvre le fichier dans l'éditeur nano (pour débutant) :

nano file\_name

Ouvre le fichier dans l'éditeur vim (pour expert) :

vim file\_name

I'm tired of seeing "can't exit vim" jokes : r/ProgrammerHumor

Chercher dans un fichier

Recherche un fichier :

grep "search\_term" file\_name

Recherche récursive :



grep -r "search\_term" directory\_name

Redirection

Redirige la sortie d'une commande dans un fichier :

command > file\_name

Ajoute la sortie de la commande à la fin du fichier :



command >> file\_name

Gestion des Processus

&#x20;Affiche les processus courant :

ps aux

Liste détaillée :



top

Nécessite l'installation du package htop, top plus lisible avec des couleurs :



htop

Tuer un processus

Arrête un processus :

kill process\_id

Forcer l'arrêt :



kill -9 process\_id

Gestion des Permissions

Change les permission d'accès d'un fichier :

chmod permissions file\_name

Ex: rwxr-xr-x (r : read, w : write, x : execute, pour le propriétaire du fichier, les membres du groupe propriétaire du fichier et tous les autres respectivement)



chmod 755 file\_name

Appliquer récursivement :



chmod -R 755 directory\_name

Changer le propriétaire

Changer le le propriétaire et le groupe du fichier :

chown user:group file\_name

Appliquer récursivement :



chown -R user:group directory\_name

Réseau

Affiche les interfaces réseaux et leurs éventuelles adresses IP

ip a

Pinger une adresse IP ou un domaine

Ping un site web :

ping example.com

Envoyer seulement 4 paquets :



ping -c 4 example.com

Vérifier les connexions réseau

Affiche les différentes connexions réseau :

sudo netstat -tulpn

Télécharger un fichier

Télécharge un fichier

wget http://example.com/file

curl -O http://example.com/file

Système

Affiche l'espace disque disponible :

*df -h*

Afficher la mémoire utilisée :



free -h

Redémarrer ou arrêter le système

Redémarre le système dans 1 minute :

sudo reboot

Redémarre le système tout de suite :

sudo shutdown -h now

Gestion des Packages (Debian/Ubuntu)

Mettre à jour la liste des packages disponibles :

sudo apt update

Mettre à jour tous les packages :



sudo apt upgrade

Installer un package :



sudo apt install package\_name

Supprimer un package :



sudo apt remove package\_name

Rechercher un package :



apt search package\_name

