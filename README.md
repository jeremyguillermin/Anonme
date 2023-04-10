# Anonme

Anonme est un outil open source écrit en Python conçu pour préserver l'anonymat des utilisateurs tout en conservant les informations nécessaires pour l'analyse des logs. Il permet de remplacer les noms d'utilisateurs, les adresses IP et les emails dans des fichiers de logs par des pseudonymes générés aléatoirement.

Anonme prend en entrée des fichiers de logs au format CSV et génère en sortie des fichiers de logs anonymisés. L'outil offre une grande flexibilité et permet aux utilisateurs de personnaliser les champs à anonymiser en modifiant le fichier de configuration. Il peut être utilisé pour anonymiser les fichiers de logs des serveurs web, des applications mobiles et des jeux en ligne.

Anonme est distribué sous licence MIT et est entièrement gratuit. Le projet est encore en développement et les contributions sont les bienvenues. Si vous avez des suggestions ou des commentaires, n'hésitez pas à ouvrir une issue sur GitHub.

# Exigences spécifiques pour fonctionner 
Il a besoin de sudo, tor, iptables et nyx pour être exécuté correctement. Il nécessite également Python 3 avec les bibliothèques subprocess, simple-term-menu, termcolor et requests.

# Installer Anonme
vous pouvez cloner le dépôt GitHub avec la commande 'git clone https://github.com/jeremyguillermin/anonme'
accéder au répertoire avec 'cd anonme' 
Exécutez 'chmod +x install.sh' pour rendre le script d'installation exécutable et exécutez-le avec './install.sh'
Pour utiliser Anonme, exécutez python3 anonme.py dans le répertoire du projet.

Anonme est distribué sous la licence GNU General Public License v3.0, ce qui signifie qu'il est libre d'utilisation, de modification et de distribution, à condition que les mêmes droits soient accordés à tous les utilisateurs.
