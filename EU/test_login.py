import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.papelerialogos.es/acceso") #para que se abra la pagina 
time.sleep(5) #el time es para que el sitio pueda cargar tranquilo
usr = driver.find_element_by_id("email") #id del input en la pagina html
usr.clear() #como para limpiar el caché
usr.send_keys("ola@gmail.com")
psw = driver.find_element_by_id("passwd") #id de la pw en la pagina html
psw.send_keys('hola1234')#envio el string
print(str) 
clk = driver.find_element_by_xpath("//*[@id='SubmitLogin']").click() #xpath del boton para que se haga click en la pagina
