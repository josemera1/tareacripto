import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.entrelineaspapeleria.cl/account/register") #para que se abra la pagina 
time.sleep(5) #el time es para que el sitio pueda cargar tranquilo
letters = string.ascii_lowercase
name = driver.find_element_by_id("FirstName")
name.send_keys("adrian")
lname = driver.find_element_by_id("LastName")
lname.send_keys("riquelme")
usr = driver.find_element_by_id("Email") #id del input en la pagina html
usr.clear() #como para limpiar el caché
usr.send_keys("asdas@gmail.com")
psw = driver.find_element_by_id("CreatePassword") #id de la pw en la pagina html
str = ''.join(random.choice(letters) for i in range(100)) #genera clave random con minimo 5, por temas de la pagina
psw.send_keys(str)#envio el string
print(str) 
clk = driver.find_element_by_xpath("//*[@id='create_customer']/p/input").click() #xpath del boton para que se haga click en la pagina
