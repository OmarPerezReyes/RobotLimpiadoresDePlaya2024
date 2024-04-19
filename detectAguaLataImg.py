import cv2
import numpy as np

# Función para detectar la tonalidad azul-celeste
def detectar_tonalidad(imagen):
    # Convertir la imagen de BGR a HSV (Hue, Saturation, Value)
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    
    # Definir el rango de tonalidades azules-celestes en HSV
    lower_azul_celeste = np.array([85, 100, 100])
    upper_azul_celeste = np.array([110, 255, 255])
    
    # Definir el rango de tonalidades negras en HSV
    lower_negro = np.array([0, 0, 0])
    upper_negro = np.array([180, 255, 20])
    
    # Aplicar la máscara para encontrar los píxeles en el rango de azul-celeste
    mask1 = cv2.inRange(hsv, lower_azul_celeste, upper_azul_celeste)
     # Aplicar la máscara para encontrar los píxeles en el rango de negro
    mask2 = cv2.inRange(hsv, lower_negro, upper_negro)
    
    
    # Calcular el porcentaje de píxeles azul-celestes
    total_pixeles = np.prod(imagen.shape[:2])
    pixeles_azul_celeste = cv2.countNonZero(mask1)
    porcentaje_azul_celeste = (pixeles_azul_celeste / total_pixeles) * 100
    
      # Calcular el porcentaje de píxeles negros

    pixeles_negros = cv2.countNonZero(mask2)
    porcentaje_negro = (pixeles_negros / total_pixeles) * 100
    
    # Aplicar la máscara a la imagen original
    #resultado = cv2.bitwise_and(imagen, imagen, mask1=mask1)
    
    # Aplicar la máscara a la imagen original
    #resultado = cv2.bitwise_and(imagen, imagen, mask2=mask2)
    
    return porcentaje_azul_celeste, porcentaje_negro
    
# Cargar la imagen de entrada
imagen = cv2.imread('lata1.jpg')


# Llamar a la función para detectar la tonalidad negra
porcentaje_azul_celeste, porcentaje_negro = detectar_tonalidad(imagen)



# Mostrar el porcentaje de tonalidad azul-celeste
print("Porcentaje de tonalidad azul-celeste en la imagen:", porcentaje_azul_celeste)
print("Porcentaje de tonalidad negra en la imagen:", porcentaje_negro)


