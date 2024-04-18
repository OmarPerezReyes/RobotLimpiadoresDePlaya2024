import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

def load_image():
    global loaded_image, img_tk, original_img
    # Abrir el cuadro de diálogo de explorador de archivos
    path = filedialog.askopenfilename()

    if path:
        # Cargar la imagen utilizando PIL
        pil_img = Image.open(path)

        # Convertir la imagen PIL a una matriz numpy (formato que OpenCV puede manejar)
        original_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

        # Escalar la imagen para que se ajuste al tamaño de la ventana
        resized_img = cv2.resize(original_img, (400, 300))

        # Convertir la imagen OpenCV a formato de imagen PIL para mostrarla en Tkinter
        img_pil = Image.fromarray(cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB))

        # Convertir la imagen PIL a formato Tkinter
        img_tk = ImageTk.PhotoImage(img_pil)

        # Actualizar la etiqueta de la imagen con la nueva imagen
        label.config(image=img_tk)
        label.image = img_tk

        # Almacenar la imagen cargada globalmente para usarla en la función de detección
        loaded_image = original_img.copy()

def detect_contours():
    global loaded_image, img_tk
    # Convertir la imagen a escala de grises
    gray_img = cv2.cvtColor(loaded_image, cv2.COLOR_BGR2GRAY)

    # Aplicar un umbral para detectar regiones negras
    _, thresh = cv2.threshold(gray_img, 30, 255, cv2.THRESH_BINARY)

    # Aplicar una operación de erosión para eliminar reflejos
    kernel = np.ones((5, 5), np.uint8)
    eroded_thresh = cv2.erode(thresh, kernel, iterations=1)

    # Encontrar contornos en la imagen umbralizada y erosionada
    contours, _ = cv2.findContours(eroded_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos encontrados sobre la imagen original
    contour_img = loaded_image.copy()
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

    # Convertir la imagen OpenCV a formato de imagen PIL para mostrarla en Tkinter
    img_pil = Image.fromarray(cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB))

    # Convertir la imagen PIL a formato Tkinter
    img_tk = ImageTk.PhotoImage(img_pil)

    # Actualizar la etiqueta de la imagen con la nueva imagen
    label.config(image=img_tk)
    label.image = img_tk

# Crear la ventana principal
root = tk.Tk()
root.title("Calibrador de Detección de Contornos")

# Crear un botón para cargar la imagen
load_button = tk.Button(root, text="Cargar Imagen", command=load_image)
load_button.pack(pady=10)

# Crear un botón para detectar los contornos en la imagen cargada
detect_button = tk.Button(root, text="Detectar Contornos", command=detect_contours)
detect_button.pack(pady=5)

# Crear una etiqueta para mostrar la imagen
label = tk.Label(root)
label.pack()

# Almacenar la imagen cargada globalmente
loaded_image = None
original_img = None
img_tk = None

# Ejecutar la aplicación
root.mainloop()
