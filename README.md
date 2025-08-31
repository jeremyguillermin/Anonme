# Anonme - Outil de Gestion Tor

Anonme est un script Python en ligne de commande conçu pour simplifier la gestion du réseau Tor sur les systèmes Linux. Il fournit une interface textuelle simple pour router l'ensemble du trafic système à travers Tor, vérifier son anonymat, et personnaliser la configuration des circuits Tor.

---

### ⚠️ Avertissement Important

-   **Privilèges Root :** Ce script modifie les règles de pare-feu du système (`iptables`) et les fichiers de configuration de Tor (`/etc/tor/torrc`). Il **doit impérativement être exécuté avec des privilèges `sudo`**.
-   **Compatibilité :** Le script est conçu pour des distributions Linux basées sur Debian (comme Ubuntu, Kali Linux, etc.) qui utilisent `apt` et le service `tor`. Il n'est pas compatible avec Windows ou macOS.
-   **Sauvegardes :** Le script crée une sauvegarde de votre configuration Tor originale (`/etc/tor/torrc.original`) avant d'appliquer une nouvelle configuration.

---

## Fonctionnalités

-   **Routage Global du Trafic :** Redirige tout le trafic de votre machine à travers le réseau Tor en une seule commande.
-   **Retour au Clearnet :** Réinitialise les règles de pare-feu et arrête le service Tor pour revenir à une connexion internet normale.
-   **Vérification de l'Adresse IP :** Affiche rapidement votre adresse IP publique et les informations de géolocalisation associées via `ipinfo.io`.
-   **Configuration Personnalisée du Circuit Tor :**
    -   Choisissez interactivement les pays pour vos nœuds d'entrée (`EntryNodes`).
    -   Choisissez les pays pour vos nœuds de sortie (`ExitNodes`).
    -   Excluez certains pays de votre circuit (`ExcludeNodes`).
-   **Suivi du Relais :** Lance l'outil `nyx` pour obtenir des informations en temps réel sur votre connexion Tor.
-   **Interface Simple :** Un menu textuel coloré pour une navigation facile.

## Prérequis

### 1. Logiciels Système

Vous devez installer `tor` et `nyx` s'ils ne sont pas déjà sur votre système.

```bash
sudo apt-get update
sudo apt-get install tor nyx
```

### 2. Bibliothèques Python

Le script utilise plusieurs bibliothèques Python qui peuvent être installées via `pip`.

```bash
pip install simple_term_menu termcolor requests
```

## Utilisation

Exécutez toujours le script avec `sudo` pour lui permettre de gérer les services et les règles de pare-feu.

```bash
sudo python votre_script.py
```

### Description des Menus

1.  **Check your IP :** Affiche votre adresse IP publique actuelle pour vérifier si vous passez bien par Tor.
2.  **Start all in Tor :** Active le service Tor et configure `iptables` pour forcer tout le trafic à passer par le réseau Tor.
3.  **Back to the Clearnet :** Restaure les `iptables` par défaut et arrête le service Tor.
4.  **Chose your Tor Configuration :** Ouvre un sous-menu pour créer une configuration personnalisée.
    -   Vous pouvez y choisir les pays pour les nœuds d'entrée, de sortie ou à exclure.
    -   Une fois votre choix fait, vous devez sélectionner **"Activate your Configuration"** pour que le script modifie le fichier `/etc/tor/torrc`.
    -   L'option **"Delete your Configuration"** restaure le fichier `torrc` original.
5.  **Information about your relay :** Lance `nyx`, un moniteur en temps réel pour votre client Tor. Appuyez sur `q` pour quitter `nyx` et revenir au menu principal.
6.  **Quit :** Quitte le script.
