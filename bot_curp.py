import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox() ##Open firefox
driver.get("https://www.gob.mx/curp/") ##Curp Page
#driver.manage().window().maximize();
#driver.set_window_size(2080,1600)
driver.maximize_window()

def buscar_curp(lista):
	for curp in lista:
		text_box = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="curpinput"]')))
		text_box=driver.find_element(By.XPATH, '//*[@id="curpinput"]')
		text_box.send_keys(curp)
		driver.execute_script("window.scrollTo(0, 200)")
		boton=driver.find_element(By.XPATH, '//*[@id="searchButton"]')
		boton.click()
		print(curp)
		driver.get("https://www.gob.mx/curp/")

lista=['AARS980525HDFLMR03', 'RALF591027MHGMPL05']
lista=lista+lista
buscar_curp(lista)
driver.quit()
