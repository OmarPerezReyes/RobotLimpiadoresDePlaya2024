import cv2
import numpy as np

# Función para detectar la tonalidad azul-celeste y negra en una imagen
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
    mask_azul_celeste = cv2.inRange(hsv, lower_azul_celeste, upper_azul_celeste)
    # Aplicar la máscara para encontrar los píxeles en el rango de negro
    mask_negro = cv2.inRange(hsv, lower_negro, upper_negro)
    
    # Calcular el porcentaje de píxeles azul-celestes y negros
    total_pixeles = np.prod(imagen.shape[:2])
    pixeles_azul_celeste = cv2.countNonZero(mask_azul_celeste)
    porcentaje_azul_celeste = (pixeles_azul_celeste / total_pixeles) * 100

    pixeles_negro = cv2.countNonZero(mask_negro)
    porcentaje_negro = (pixeles_negro / total_pixeles) * 100
    
    return porcentaje_azul_celeste, porcentaje_negro

# Inicializar la cámara web
cam = cv2.VideoCapture(0)

# Inicializar el contador
contador = 0

while True:
    # Capturar imagen de la cámara
    ret, frame = cam.read()
    
    # Incrementar el contador
    contador += 1
    
    # Revisar la tonalidad cada 10 frames
    if contador == 30:
        # Llamar a la función para detectar la tonalidad azul-celeste y negra
        porcentaje_azul_celeste, porcentaje_negro = detectar_tonalidad(frame)

        # Mostrar el porcentaje de tonalidad azul-celeste y negra
        #print("Porcentaje de tonalidad azul-celeste en el imagen:", porcentaje_azul_celeste)
        #print("Porcentaje de tonalidad negra en la imagen:", porcentaje_negro)
        
        if(porcentaje_azul_celeste>.50){
            print("AGUA");
        }
        
        if(porcentaje_negro>.30){
            print("LATA");
        }
        
        # Reiniciar el contador
        contador = 0

    # Mostrar la imagen
    cv2.imshow('Frame', frame)
    
    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas
cam.release()
cv2.destroyAllWindows()

