# ApexLytics

ApexLytics est un outil de suivi des statistiques des joueurs d'Apex Legends, permettant d'afficher leur classement, leur progression et diverses informations utiles en temps réel.

## 🚀 Fonctionnalités

- Recherche des statistiques d'un joueur en fonction de son pseudo et de sa plateforme (PC, PlayStation, Xbox).
- Affichage du rang classé et des points RP du joueur.
- Estimation du prochain rang et du risque de rétrogradation.
- Calcul du niveau total du joueur en prenant en compte le prestige.
- Génération automatique du badge de niveau via l'API d'Apex Legends Status.
- Interface responsive et intuitive.

## 🛠️ Technologies utilisées

- **Frontend :** HTML, CSS, JavaScript
- **Backend :** Flask (Python) pour récupérer les données depuis l'API
- **API :** [Apex Legends Status API](https://apexlegendsstatus.com/) pour les statistiques des joueurs
- **Versioning :** Git & GitHub

## 📦 Installation & Exécution

### 1️⃣ Cloner le projet

```bash
 git clone https://github.com/Skillisgod/ApexLytics.git
 cd ApexLytics
```

### 2️⃣ Installer les dépendances

Assurez-vous d'avoir **Python 3** et **pip** installés.

```bash
pip install flask requests
```

### 3️⃣ Ajouter votre clé API

Pour utiliser l'API, vous devez générer une clé sur le site suivant : [Apex Legends API Portal](https://portal.apexlegendsapi.com/)

Une fois obtenue, ajoutez votre clé dans `main.py` à l'emplacement prévu.

### 4️⃣ Lancer le serveur backend

```bash
python main.py
```

### 5️⃣ Ouvrir le site

Accédez à `http://127.0.0.1:5000/` dans votre navigateur.

### 6️⃣ Tester le site

Vous pouvez renseigner le nom de joueur suivant ainsi que la plateforme qui correspond.

- **Pseudo :** Louis XIV  
- **Plateforme :** PC

## 🖼️ Aperçu

![image](https://github.com/user-attachments/assets/01b4ee36-6a7f-4ceb-be57-4a4d988cc8fb)


## 📜 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus d’informations.

