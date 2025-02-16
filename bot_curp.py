import pandas as pd
import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox() ##Open firefox
#driver.get("https://www.gob.mx/curp/") ##Curp Page
driver.maximize_window()

def buscar_curp(lista):
	for curp in lista:
		driver.get("https://www.gob.mx/curp/")
		text_box = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="curpinput"]')))
		text_box=driver.find_element(By.XPATH, '//*[@id="curpinput"]')
		text_box.send_keys(curp)
		driver.execute_script("window.scrollTo(0, 200)")
		boton=driver.find_element(By.XPATH, '//*[@id="searchButton"]')
		boton.click()
		time.sleep(5)
		books = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "panel-body")))
		driver.execute_script("window.scrollTo(0, 200)")
		df_list = []
		for i, book in enumerate(books):
			splited = books[i].text.split("\n")
			for i in splited:
				datos = i.split(':')
				df_list.append(datos[1])
		df = pd.DataFrame()
		df['curp']=[df_list[0]]
		df['nombre']=[df_list[1]]
		df['ap_paterno']=[df_list[2]]
		df['ap_materno']=[df_list[3]]
		df['sexo']=[df_list[4]]
		df['fecha_nacimiento']=[df_list[5]]
		df['nacionalidad']=[df_list[6]]
		df['entidad_nacimiento']=[df_list[7]]
		print(df.head())

lista=['AARS980525HDFLMR03', 'RALF591027MHGMPL05']
buscar_curp(lista)
driver.quit()
