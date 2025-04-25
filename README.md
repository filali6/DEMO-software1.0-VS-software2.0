```markdown
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
```

**Fonctionnement du script** :

1. Chargement de l’image avec OpenCV.
2. Conversion en niveaux de gris (`cv2.cvtColor`).
3. Détection des contours avec l’algorithme **Canny** :
   - `cv2.Canny(gray, 100, 200)` détecte les variations brusques d’intensité (bords).
4. Recherche de formes continues avec `cv2.findContours` :
   - Transforme les pixels détectés en **contours exploitables**.
5. Affichage de l’image avec les **contours dessinés** en vert.

> ✅ Ce script illustre une méthode **déterministe**, où l’on code manuellement les étapes du traitement.  
> ❌ Il ne reconnaît pas les objets (ex : il voit un contour, mais ne sait pas que c’est un chien ou une voiture).

---

### 🤖 Software 2.0 : Approche basée sur l’IA (YOLOv3)

Ce script applique un modèle d’intelligence artificielle pré-entraîné pour **reconnaître les objets** dans l’image.

```bash
python software2.0.py
```

**Fonctionnement du script** :

1. Chargement du modèle YOLO (`.cfg` et `.weights`) avec OpenCV DNN.
2. Lecture de l’image et transformation en **blob** :
   - Mise à l’échelle, normalisation, etc. (`cv2.dnn.blobFromImage`).
3. Passage de l’image dans le réseau (`net.forward(...)`).
4. Analyse des prédictions :
   - Pour chaque boîte proposée, on récupère la **classe la plus probable** et sa **confiance**.
   - Si confiance > 0.5 → affichage d’un **rectangle vert** avec le **nom de l’objet détecté**.
5. Affichage de l’image annotée avec les objets reconnus.

> ✅ Cette méthode est **probabiliste et intelligente** : elle détecte et **reconnaît** les objets dans la scène.  
> 🤯 Exemple : le réseau peut détecter une “person”, une “dog” ou une “bicycle”, car il a appris cela à partir de milliers d’images.

---

## ⚖️ Comparaison Résumée

| Critère               | Software 1.0                       | Software 2.0                            |
|-----------------------|------------------------------------|-----------------------------------------|
| Méthode               | Traitement d’image classique       | Intelligence artificielle (YOLOv3)      |
| Reconnaissance        | Aucune                             | Oui, objets nommés et localisés         |
| Code écrit à la main  | Oui (règles explicites)            | Non (réseau appris à partir de données) |
| Flexibilité           | Faible                             | Très élevée                              |
| Compréhension de scène| Non                                | Oui                                      |

---

## 🧠 Conclusion

Cette démo permet de visualiser la différence entre :
- **Programmer pour dire à la machine comment faire** (Software 1.0)
- **Entraîner la machine à apprendre à faire** (Software 2.0)

Elle illustre parfaitement le passage du **code explicite** à l’**intelligence apprise**, cœur du concept de **Software 2.0**.
```
