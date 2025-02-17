import cv2
import tkinter as tk
import pandas as pd
from tkinter import filedialog
from PIL import Image, ImageTk
from bot_curp import search_curp
from ocr_curp import find_curp
from img_comparison import compare

cap = cv2.VideoCapture(0)

def mostrar_video():
	global cap
	# Leer el frame actual de la cámara
	ret, frame = cap.read()
	# Convertir el frame a una imagen que pueda ser mostrada en la ventana
	img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	img2 = Image.fromarray(img2)
	imgtk = ImageTk.PhotoImage(image=img2)
	# Mostrar la imagen en la ventana
	label_video.config(image=imgtk)
	label_video.image = imgtk
	# Repetir el proceso para mostrar el video en tiempo real
	frame3.after(10, mostrar_video)

def mostrar_ventana4():
	global img
	frame3.pack_forget()
	ret, frame = cap.read()
	# Convertir el frame a una imagen que pueda ser mostrada en la ventana
	img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	similarity = compare(img, img2)
	if similarity>0.35:
		label = tk.Label(frame4, text='Se confirmó su identidad, comenzando solicitud', font = ('Arial',20))
		label.pack()
		frame4.pack(fill="both", expand=True)
	else:
		label = tk.Label(frame0, text='No se pudo confirmar su identidad, intente de nuevo ', font = ('Arial',20))
		label.pack()
		frame0.pack(fill="both", expand=True)

def mostrar_ventana3():
	frame2.pack_forget()
	frame3.pack(fill="both", expand=True)

def mostrar_ventana1():
    frame0.pack_forget()
    frame1.pack(fill="both", expand=True)

def mostrar_ventana2():
	global img,msg
	frame1.pack_forget()  # Oculta la ventana 1
	curp=find_curp(img)
	df=search_curp([curp])
	if  df.iloc[0,4]=='HOMBRE':
		msg='Bienvenido '+df.iloc[0,1]
	else:
		msg='Bienvenida '+df.iloc[0,1]
	apellido1='Apellido Paterno: '+df.iloc[0,2]
	apellido2='Apellido Materno: '+df.iloc[0,3]
	fecha='Fecha de Nacimiento: '+df.iloc[0,5]
	#print(df)
	label = tk.Label(frame2, text=msg, font = ('Arial',20))
	label.pack()
	labelapellido = tk.Label(frame2, text=apellido1, font = ('Arial',20))
	labelapellido.pack()
	labelapellido = tk.Label(frame2, text=apellido2, font = ('Arial',20))
	labelapellido.pack()
	labelfecha = tk.Label(frame2, text=fecha, font = ('Arial',20))
	labelfecha.pack()
	labelx = tk.Label(frame2, text='Presiona continuar si tus datos son correctos', font=('Arial',20))
	labelx.pack()
	button2 = tk.Button(frame2, text="Continuar",command=mostrar_ventana3, activebackground="#F50743")
	button2.pack()
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
label_imagen1 = tk.Label(frame1, text='INE')
label_imagen1.pack()
button1_1 = tk.Button(frame1, text="Continuar", command=mostrar_ventana2, activebackground="#F50743").pack()
frame1.pack(fill="both", expand=True)  # Mostrar al inicio

##Window 2
frame2 = tk.Frame(root)

##Window 3
frame3 = tk.Frame(root)
button3 = tk.Button(frame3, text="Abrir camara", command=mostrar_video, activebackground="#F50743").pack()
button3 = tk.Button(frame3, text="Tomar foto", command=mostrar_ventana4, activebackground="#F50743").pack()
label_video = tk.Label(frame3)
label_video.pack()

frame0 = tk.Frame(root)
button0 = tk.Button(frame0, text="Continuar", command=mostrar_ventana1, activebackground="#F50743").pack()

frame4 = tk.Frame(root)

root.mainloop()
