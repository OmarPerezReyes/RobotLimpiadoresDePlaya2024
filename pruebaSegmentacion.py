import cv2
import numpy as np

# Función para detectar la tonalidad azul-celeste
def detectar_azul_celeste(imagen):
    # Convertir la imagen de BGR a HSV (Hue, Saturation, Value)
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    
    # Definir el rango de tonalidades azules-celestes en HSV
    lower_azul_celeste = np.array([85, 100, 100])
    upper_azul_celeste = np.array([110, 255, 255])
    
    # Aplicar la máscara para encontrar los píxeles en el rango de azul-celeste
    mask = cv2.inRange(hsv, lower_azul_celeste, upper_azul_celeste)
    
    # Calcular el porcentaje de píxeles azul-celestes
    total_pixeles = np.prod(imagen.shape[:2])
    pixeles_azul_celeste = cv2.countNonZero(mask)
    porcentaje_azul_celeste = (pixeles_azul_celeste / total_pixeles) * 100
    
    # Aplicar la máscara a la imagen original
    resultado = cv2.bitwise_and(imagen, imagen, mask=mask)
    
    return porcentaje_azul_celeste, resultado

# Cargar la imagen de entrada
imagen = cv2.imread('arena1.jpg')

# Llamar a la función para detectar la tonalidad azul-celeste
porcentaje_azul_celeste, imagen_salida = detectar_azul_celeste(imagen)

# Mostrar el porcentaje de tonalidad azul-celeste
print("Porcentaje de tonalidad azul-celeste en la imagen:", porcentaje_azul_celeste)

# Mostrar la imagen de salida
cv2.imshow('Imagen de salida', imagen_salida)
cv2.waitKey(0)

# Cerrar todas las ventanas abiertas antes de finalizar el programa
cv2.destroyAllWindows()

