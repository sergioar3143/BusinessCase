import cv2
import tkinter as tk
import pandas as pd
from tkinter import filedialog
from PIL import Image, ImageTk
from bot_curp import search_curp
from ocr_curp import find_curp

def mostrar_ventana2():
	global img,msg
	frame1.pack_forget()  # Oculta la ventana 1
	curp=find_curp(img)
	df=search_curp([curp])
	msg='Bienvenido '+df.iloc[0,1]
	label = tk.Label(frame2, text=msg)
	label.pack()
	button2 = tk.Button(frame2, text="Cargar imagen",command=lambda:cargar_imagen('Cargar imagen',label_imagen2), activebackground="#F50743")
	button2.pack()
	label_imagen2 = tk.Label(frame2, text=msg)
	label_imagen2.pack()
	frame2.pack(fill="both", expand=True)  # Muestra la ventana 2

def cargar_imagen(text, label):
	global img
	ruta = filedialog.askopenfilename(title=text, filetypes=[("Imágenes", ".jpg .jpeg .png .bmp")])
	if ruta:
		img = cv2.imread(ruta)
		imagen = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		imagen = Image.fromarray(imagen)
		imagen_tk = ImageTk.PhotoImage(imagen)
		label.config(image=imagen_tk)
		label.image = imagen_tk
		if text=='Cargar INE':
			print("hola")
		else:
			img2=imagen

root = tk.Tk()
root.geometry("1500x1000")
root.title("Validar sujeto")

##Window 1
frame1 = tk.Frame(root)
button1 = tk.Button(frame1, text="Cargar INE",command=lambda:cargar_imagen('Cargar INE',label_imagen1), activebackground="#F50743")
button1.pack()

#button1_1=tk.Button(frame1, text="Continuar", command=mostrar_ventana2).pack()
label_imagen1 = tk.Label(frame1, text='INE')
label_imagen1.pack()

button1_1=tk.Button(frame1, text="Continuar", command=mostrar_ventana2, activebackground="#F50743").pack()


frame1.pack(fill="both", expand=True)  # Mostrar al inicio

##Window 2
frame2 = tk.Frame(root)

root.mainloop()
