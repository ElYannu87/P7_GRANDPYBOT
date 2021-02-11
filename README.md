
# P7_GRANDPYBOT  
  

## **Projet-7 : Créez GrandPyBot, le papy robot**

Ce projet est le 7ème projet de La formation de développeur d'application en python auprès de l'établissement OpenClassrooms.  
  

## 1 Informations générales

  
**1.1 Description du projet**  
Le but du projet est de créer une page web avec le framework python "flask" où l'utilisateur pourrait discuter avec un robot, "GrandPy Bot" et lui demander des informations sur le lieu de son choix. Ce robot doit alors lui retourner un ensemble d'informations à propos de ce lieu.  
  
**1.2 Description du parcours utilisateur**  
L'utilisateur entre l'url de la page web correspondante au projet. Il arrive alors sur une page web contenant une zone de chat et une zone où il peut écrire sa question. L'utilisateur introduit alors sa question et appuie sur le bouton "envoyer". Il y a alors 3 possibilités:  
  
Le robot a compris la question et lui affiche les informations venant des différentes API utilisées.  
Le robot a compris la question mais les API ne renvoient pas les informations attendues. Le robot répond à l'utilisateur qu'il n'a rien trouvé sur le lieu en question  
Le robot n'a pas compris la question et demande à l'utilisateur d'être plus clair sur le lieu demandé  

**1.3 Fonctionnalités du projet**  
Interactions en AJAX : l'utilisateur envoie sa question en appuyant sur entrée et la réponse s'affiche directement dans l'écran, sans recharger la page.  
Utilisation de l'API de HERE et celle de Media Wiki.  
Rien n'est sauvegardé. Si l'utilisateur charge de nouveau la page, tout l'historique est perdu.  


## 2 Prérequis pour l'utilisation du projet

**2.1 Langages utilisés**  
le langage de programmation utilisé dans ce projet est python. Les langages pour la partie "web" sont le HTML, le CSS et le javascript  
Lien pour télécharger [PYTHON](https://www.python.org/downloads/)  
version de python lors du développement : 3.9
  
**2.2 librairies utilisées:**  
Vous pouvez retrouver l'ensemble des librairies utilisées pour ce projet dans le fichier requirements.txt et tout installer directement via ce fichier grâce à une commande pip.  

    pip install requirements.txt

  
**2.3 Utilisation des clefs d'API**  
Pour des raisons de sécurité, les clefs de l'API ne sont pas inclus dans ce projet. Afin d'utiliser l'application vous devez créer un fichier nommé "config.py" dans la racine du projet. Ensuite vous rajouté `GOOGLE_APP_ID ='YourKey'`  à ce fichier. 

**2.4 Lancer l'application**
Pour lancer l'application exécuter la commande suivante :

    python run.py

  

## 3 Structure du projet

Organisation du projet : 
  
dossier "gpbapp" : contient le code source du projet  
dossier "tests" : contient les tests liés au projet.  
fichier ".gitignore" : permet à certains fichiers et dossiers de ne pas être "suivi" par git  
fichier "run.py" : fichier permettant de lancer l'application
fichier "README.md" : ce fichier  
fichier "requirements.txt" : contient les différentes librairies utilisées par le projet  
fichier "Procfile" : Ce fichier est nécessaire pour l'hébergement sur Heroku

**3.1 Dossier "app"**  
Contient le code source du projet  
  
**3.1.1 Dossier "static"**  
Celui-ci contient les fichiers css, le fichier javascript  utilisées dans ce projet. 
  
**3.1.2 Dossier templates**  
Celui-ci contient le fichier index.html
  
**3.1.3 Dossier utils**  
Ce dossier contient les fichiers : googleapi.py, wikiapi.py parser.py et stop_words_fr.json 
 
**3.1.3.1 Fichier googleapi.py**
Traite la recherche de l'utilisateur pour faire une requête auprès de l'api de googlegeocode.

**3.1.3.2 Fichier wikiapi.py**
Traite la recherche de l'utilisateur pour faire une requête auprès de l'api de wikipedia.
  
**3.1.3.3 Fichier parser.py**  
Traite l'analyse de la question de l'utilisateur afin d'en retirer les informations nécessaires.  
  
**3.1.4 Fichier views.py**  
Contient toute la partie de Flask et gère les point entrant et sortant de notre application.
  
  

## 4 Informations complémentaires

**4.1. Acteurs**  
Développeur : Yannick Driever
  
**4.1 Déploiement**  
L'application est déployé avec Heroku vous pouvez retrouvé l'application à cette adresse : https://grandpybotprojet7.herokuapp.com/
  
