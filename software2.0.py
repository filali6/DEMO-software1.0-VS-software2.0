import cv2
import numpy as np

# Charger le modèle YOLO pré-entraîné
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Charger les noms des classes (ex: personne, voiture, chat, etc.)
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Récupérer les couches de sortie du modèle YOLO
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Charger l'image
image = cv2.imread("image.jpg")
height, width, channels = image.shape

# Prétraiter l'image pour YOLO
blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)

# Listes pour stocker les résultats
class_ids = []
confidences = []
boxes = []

# Parcourir chaque détection
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > 0.5:  # Seuil de confiance (ajuster si nécessaire)
            # Récupérer les coordonnées de l'objet
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Appliquer Non-Maximum Suppression (NMS) pour éviter les doublons
indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# Affichage des objets détectés
for i in indices.flatten():
    x, y, w, h = boxes[i]
    label = f"{classes[class_ids[i]]}: {confidences[i]:.2f}"  # Nom + Confiance
    color = (0, 255, 0)  # Vert

    # Dessiner un rectangle autour de l'objet
    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
    cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
image_resized = cv2.resize(image, (800, 600))

# Afficher l'image redimensionnée
cv2.imshow("Image Redimensionnée", image_resized)
# Afficher l'image finale avec les détections
#cv2.imshow("YOLO Object Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
