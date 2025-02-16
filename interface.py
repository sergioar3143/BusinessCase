import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

global img1,img2

def cargar_imagen(text, label):
	ruta = filedialog.askopenfilename(title=text, filetypes=[("Imágenes", ".jpg .jpeg .png .bmp")])
	if ruta:
		imagen = cv2.imread(ruta)
		imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
		imagen = Image.fromarray(imagen)
		imagen_tk = ImageTk.PhotoImage(imagen)
		label.config(image=imagen_tk)
		label.image = imagen_tk
		if text=='Cargar INE':
			img1=imagen
		else:
			img2=imagen

ventana = tk.Tk()
ventana.geometry("1500x1000")
ventana.title("Cargar imágenes")

button1 = tk.Button(ventana, text="Cargar INE",command=lambda:cargar_imagen('Cargar INE',label_imagen1), activebackground="#F50743")
button1.pack()

label_imagen1 = tk.Label(ventana, text='INE')
label_imagen1.pack()

button2 = tk.Button(ventana, text="Cargar imagen",command=lambda:cargar_imagen('Cargar imagen',label_imagen2), activebackground="#F50743")
button2.pack()

label_imagen2 = tk.Label(ventana, text='Imagen')
label_imagen2.pack()

ventana.mainloop()
