# Vérification du Réseaux et récupération de l'adresse IP du Raspberry Pi

Vérifiez que la Raspberry Pi est active et accessible sur votre réseau local en interrogeant son nom d'hôte :

```bash
ping startracker
```
Récupérer son adresse IP en utilisant la commande suivante :

```bash
Resolve-DnsName startracker -Type A
```

# 2. Configuration de Visual Studio Code pour la connexion SSH

1. Ouvrez Visual Studio Code.
2. Installez l'extension "Remote - SSH" si ce n'est pas déjà fait.
3. Si vous avez déjà configuré une connexion SSH, cliquez sur l'icône "Remote Explorer" dans la barre latérale gauche. C'est Fini.
4. Si vous n'avez pas encore configuré de connexion SSH, cliquez sur l'icône "Remote Explorer" dans la barre latérale gauche, puis cliquez sur "Add New SSH Host". ou bien Tapez `ssh` ou `remote`, puis sélectionnez l'option `Remote-SSH: Add New SSH Host`
5. Entrez l'adresse IP de votre Raspberry Pi dans le format suivant : `ssh starstracker@<adresseIPV4> -A`

# 3 . Connexion à la Raspberry Pi via SSH

1. Le mot de passe est demandé lors de la première connexion. Entrez le mot de passe de l'utilisateur `starstracker` qui est configuré sur la Raspberry Pi.
2. Une fois connecté, vous pouvez exécuter des commandes sur la Raspberry Pi à distance depuis Visual Studio Code.
3. Un dossier de travail est créé sur la Rasberry pour stocker les fichiers du projet. Vous pouvez naviguer dans ce dossier 'StarTracker' et ouvrir des fichiers pour les éditer directement depuis Visual Studio Code.