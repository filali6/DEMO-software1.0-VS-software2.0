import cv2

# Charger l'image
image = cv2.imread('image.jpg')

# Convertir en niveaux de gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Appliquer le Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Trouver les contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dessiner les contours sur l'image
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Afficher l'image avec contours détectés
image_resized = cv2.resize(image, (800, 600))

# Afficher l'image redimensionnée
cv2.imshow("Image Redimensionnée", image_resized)

#cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
