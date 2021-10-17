import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.entrelineaspapeleria.cl/account/login?return_url=%2Faccount#recover") #para que se abra la pagina 
time.sleep(5) #el time es para que el sitio pueda cargar tranquilo
letters = string.ascii_lowercase
usr = driver.find_element_by_id("RecoverEmail") #id del input en la pagina html
usr.clear() #como para limpiar el caché
usr.send_keys("asdasd@gmail.com")
clk = driver.find_element_by_xpath("//*[@id='RecoverPasswordForm']/div/form/p/button").click() #xpath del boton para que se haga click en la pagina
