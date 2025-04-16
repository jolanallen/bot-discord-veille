# Discord RSS Bot

Ce projet est un bot Discord qui récupère automatiquement des flux RSS provenant de diverses sources, et publie les nouveaux articles sur des canaux spécifiques de votre serveur Discord.

## Fonctionnalités

- Récupère des flux RSS sur différents sujets comme la cybersécurité, la technologie, les cryptomonnaies, les actions, etc.
- Publie automatiquement les articles dans les canaux Discord configurés.
- Évite la duplication des articles en suivant les liens déjà envoyés.
- La fréquence de récupération des flux peut être personnalisée.
- Utilise **Python** avec les bibliothèques **discord.py** et **feedparser** pour analyser les flux RSS.

## Prérequis

Avant de pouvoir utiliser ce bot, assurez-vous d'avoir installé Python et les bibliothèques nécessaires.

### Installation de Python

Assurez-vous que Python 3.8+ est installé sur votre machine. Vous pouvez télécharger la dernière version de Python sur [python.org](https://www.python.org/downloads/).

### Installation des dépendances

Clonez ce dépôt et installez les dépendances avec pip :

```bash
git clone https://github.com/jolanallen/bot-discord-veille.git
cd discord-rss-bot
pip install -r requirements.txt
