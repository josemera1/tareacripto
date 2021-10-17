import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.papelerialogos.es/recuperar_pass") #para que se abra la pagina 
time.sleep(5) #el time es para que el sitio pueda cargar tranquilo
letters = string.ascii_lowercase
usr = driver.find_element_by_id("email") #id del input en la pagina html
usr.clear() #como para limpiar el caché
usr.send_keys("asdasd@gmail.com")
clk = driver.find_element_by_xpath("//*[@id='registro']/div/form/fieldset/div[2]/button").click() #xpath del boton para que se haga click en la pagina
