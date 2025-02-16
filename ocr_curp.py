from bot_curp import buscar_curp
import easyocr
import cv2
import pandas as pd
import pytesseract
import re

def replace_curp(cadena):
	cadena=cadena.strip()
	cadena1=cadena[:4].replace('0','O').replace('5','S')
	cadena2=cadena[4:10].replace('O','0').replace('S','5')
	cadena3=cadena[10:16].replace('0','O').replace('5','S')
	cadena4=cadena[16:].replace('O','0').replace('S','5')
	return cadena1+cadena2+cadena3+cadena4

def find_curp(img):
	img_cv = cv2.imread(img)
	print('Pytesseact')

	# By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
	# we need to convert from BGR to RGB format/mode:
	img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
	result=pytesseract.image_to_string(img_rgb, lang='spa')
	result=result.split(' ')

	for i in result:
		i=replace_curp(i)
		m = re.search('[A-Z]{4}\d{6}[A-Z]{6}.*',i)
		if not(m) is None:
			return i

	print('Easyocr')
	reader = easyocr.Reader(['es']) # this needs to run only once to load the model into memory
	result = reader.readtext(img_rgb, detail=0)

	for i in result:
		i=replace_curp(i)
		m = re.search('[A-Z]{4}\d{6}[A-Z]{6}.*',i)
		if not(m) is None:
			return i

curp=find_curp('ine1.jpeg')
buscar_curp([curp])

