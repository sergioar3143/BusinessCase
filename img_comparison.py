import insightface
import numpy as np
import cv2

# Cargar el modelo de reconocimiento facial
model = insightface.app.FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
model.prepare(ctx_id=0)

# Cargar y procesar las imágenes
def get_embedding(img_path):
    img = cv2.imread(img_path)
    faces = model.get(img)
    if len(faces) == 0:
        return None
    return faces[0].embedding  # Embedding de la cara detectada

emb1 = get_embedding("ine3.jpeg")
emb2 = get_embedding("foto.jpeg")

print(emb1.shape)
print(emb2.shape)

if emb1 is not None and emb2 is not None:
    similarity = np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
    print(f"Similitud: {similarity}")
else:
    print("No se detectaron rostros en una de las imágenes.")
