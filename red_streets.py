import cv2
import numpy as np
import matplotlib.pyplot as plt

def resaltar_colores_en_area(image_path, colores_hex, area_coords, output_path=None):
    """
    Resalta colores específicos dentro de un área delimitada en la imagen.
    
    :param image_path: Ruta de la imagen a procesar.
    :param colores_hex: Lista de colores en formato hexadecimal.
    :param area_coords: Coordenadas del área (x1, y1, x2, y2).
    :param output_path: Ruta opcional para guardar la imagen resultante.
    """
    # Cargar la imagen en formato BGR
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        print("Error: No se pudo cargar la imagen. Verifica la ruta.")
        return
    
    # Convertir la imagen de BGR a RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Extraer la región de interés (ROI) usando las coordenadas
    x1, y1, x2, y2 = area_coords
    roi = image_rgb[y1:y2, x1:x2]

    # Convertir los colores HEX a RGB
    colores_rgb = [tuple(int(color[i:i+2], 16) for i in (1, 3, 5)) for color in colores_hex]

    # Crear una máscara para los colores específicos dentro del ROI
    mask = np.zeros(roi.shape[:2], dtype=np.uint8)
    for color in colores_rgb:
        lower_bound = np.array([c - 10 for c in color], dtype=np.uint8)
        upper_bound = np.array([c + 10 for c in color], dtype=np.uint8)
        color_mask = cv2.inRange(roi, lower_bound, upper_bound)
        mask = cv2.bitwise_or(mask, color_mask)

    # Resaltar las áreas coincidentes en rojo
    roi[mask > 0] = [255, 0, 0]

    # Reintegrar la región modificada a la imagen original
    highlighted_image = image_rgb.copy()
    highlighted_image[y1:y2, x1:x2] = roi

    # Mostrar la imagen resultante
    plt.figure(figsize=(12, 8))
    plt.imshow(highlighted_image)
    plt.title("Colores Resaltados en el Área Delimitada")
    plt.axis("off")
    plt.show()

    # Guardar la imagen si se especifica una ruta
    if output_path:
        cv2.imwrite(output_path, cv2.cvtColor(highlighted_image, cv2.COLOR_RGB2BGR))
        print(f"Imagen guardada en: {output_path}")

# Ejemplo de uso
image_path = "sustainability-12-01336-g001.jpg"  # Ruta de la imagen
colores_hex = ["#A19E97", "#B4B4B4", "#C8C8C8"]  # Colores a resaltar
area_coords = (130, 365, 3250, 1490)  # Coordenadas aproximadas del área (x1, y1, x2, y2)
output_path = "colores_resaltados_area.jpg"  # Opcional: guarda la imagen

resaltar_colores_en_area(image_path, colores_hex, area_coords, output_path)



