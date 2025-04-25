# 🧠 Démo : Software 1.0 vs Software 2.0 – Détection d’Objets

Cette démo a pour but de comparer deux approches de la détection d'objets dans une image :  
- **Software 1.0** : Programmation classique basée sur des règles explicites (ex : détection de contours avec OpenCV).  
- **Software 2.0** : Programmation moderne basée sur l'apprentissage automatique (ex : détection d’objets avec un réseau YOLOv3).

---

## 📁 Contenu du projet

Le projet contient les fichiers suivants :

- `image.jpg` : Image d'exemple à tester.
- `software1.0.py` : Code Python qui applique le traitement d'image classique (Canny + findContours).
- `software2.0.py` : Code Python qui utilise un modèle d'intelligence artificielle YOLOv3 pour détecter les objets.
- `yolov3.cfg` : Fichier de configuration du modèle YOLO.
- `yolov3.weights` : Poids du réseau YOLOv3 préentraîné sur COCO.
- `coco.names` : Liste des noms de classes (person, dog, car...).
- `README.md` : Ce fichier explicatif.

---

## ▶️ Exécution des codes

### 🛠 Software 1.0 : Approche classique

Ce code détecte uniquement les contours dans l’image.  
Il n’y a pas de reconnaissance d’objet, seulement des formes géométriques basées sur les changements d’intensité.

```bash
python software1.0.py
