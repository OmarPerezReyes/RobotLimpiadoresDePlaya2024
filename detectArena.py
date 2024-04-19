import cv2
import numpy as np

# Función para detectar la tonalidad negra
def detectar_negro(imagen):
    # Convertir la imagen de BGR a HSV (Hue, Saturation, Value)
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    
    # Definir el rango de tonalidades negras en HSV
    lower_negro = np.array([0, 0, 0])
    upper_negro = np.array([180, 255, 20])
    
    # Aplicar la máscara para encontrar los píxeles en el rango de negro
    mask = cv2.inRange(hsv, lower_negro, upper_negro)
    
    # Calcular el porcentaje de píxeles negros
    total_pixeles = np.prod(imagen.shape[:2])
    pixeles_negros = cv2.countNonZero(mask)
    porcentaje_negro = (pixeles_negros / total_pixeles) * 100
    
    # Aplicar la máscara a la imagen original
    resultado = cv2.bitwise_and(imagen, imagen, mask=mask)
    
    return porcentaje_negro, resultado

# Cargar la imagen de entrada
imagen = cv2.imread('lata2.jpg')

# Llamar a la función para detectar la tonalidad negra
porcentaje_negro, imagen_salida = detectar_negro(imagen)

# Mostrar el porcentaje de tonalidad negra
print("Porcentaje de tonalidad negra en la imagen:", porcentaje_negro)

# Mostrar la imagen de salida
cv2.imshow('Imagen de salida', imagen_salida)
cv2.waitKey(0)

# Cerrar todas las ventanas abiertas antes de finalizar el programa
cv2.destroyAllWindows()

