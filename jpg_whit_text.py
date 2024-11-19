import cv2
from google.colab.patches import cv2_imshow
def img ():
  image = cv2.imread('output.png', cv2.IMREAD_UNCHANGED)
  back = cv2.imread('/content/galaxia.jpeg')
  result = change_back(back, image)

  # Guardar el resultado en un archivo
  output_file = '/content/resultado_final.jpg'  # Ruta y nombre del archivo
  cv2.imwrite(output_file, result)  # Guarda la imagen en la ruta especificada
img()
image = cv2.imread('resultado_final.jpg')
# La cadena de texto
text = "When programas estilo libre"
# Tge font
font = cv2.FONT_HERSHEY_SIMPLEX
# El tamaño de la fuente
font_scale = 1
# El color en el formato RGB (Azul, Verde, Rojo).
# Este es el color blanco
color = (255, 255, 255)
# La delgadez de la línea
thickness = 2
image_with_text = cv2.putText(image, text, (650, 100), font, font_scale, color, thickness, cv2.LINE_AA)

cv2_imshow(image_with_text)
cv2.imwrite('resultado_final.jpg',image_with_text)
