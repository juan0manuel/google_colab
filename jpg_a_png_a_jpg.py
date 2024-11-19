from rembg import remove
import numpy as np
from google.colab.patches import cv2_imshow
import cv2

input_path = './Tortuga.jpeg'
output_path = 'output.png'
with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)
cv2_imshow(cv2.imread('output.png'))

def change_back(background, img):
    """ Una función que reemplaza el fondo negro de las imágenes por otra imagen.
    Acepta dos argumentos: la imagen de fondo (background) y la propia imagen (img).
    La función comenzará desde la esquina superior izquierda de la imagen.
    Buscará todos los píxeles negros (con el valor 0) y los reemplazará por píxeles de la imagen de fondo."""

    background = cv2.resize(background, (img.shape[1], img.shape[0]), interpolation = cv2.INTER_AREA)
    res = np.copy(background)
    x, y = 0, 0
    place = res[y: y + img.shape[0], x: x + img.shape[1]]
    a = img[..., 3:].repeat(3, axis=2).astype('uint16')
    place[...] = (place.astype('uint16') * (255 - a) // 255) + img[..., :3].astype('uint16') * a // 255
    return res

image = cv2.imread('output.png', cv2.IMREAD_UNCHANGED)
back = cv2.imread('/content/galaxia.jpeg')
result = change_back(back, image)

# Guardar el resultado en un archivo
output_file = '/content/resultado_final.jpg'  # Ruta y nombre del archivo
cv2.imwrite(output_file, result)  # Guarda la imagen en la ruta especificada

# Confirmar guardado mostrando el archivo guardado
cv2_imshow(cv2.imread(output_file))
