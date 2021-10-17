import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.papelerialogos.es/registro") #para que se abra la pagina 
time.sleep(5) #el time es para que el sitio pueda cargar tranquilo
letters = string.ascii_lowercase
name = driver.find_element_by_xpath("//*[@id='center_column']/div/div/form/div/fieldset/div[1]/div[1]/input")
name.send_keys("adrian")
mail = driver.find_element_by_xpath("//*[@id='center_column']/div/div/form/div/fieldset/div[1]/div[2]/input")
mail.send_keys("asdasda12@gmail.com")
psw = driver.find_element_by_xpath("//*[@id='center_column']/div/div/form/div/fieldset/div[1]/div[3]/input") #id de la pw en la pagina html
str = ''.join(random.choice(letters) for i in range(255)) #genera clave random con minimo 5, por temas de la pagina
psw.send_keys(str+'13')#envio el string
psw1 = driver.find_element_by_xpath("//*[@id='center_column']/div/div/form/div/fieldset/div[1]/div[4]/input") #id de la pw en la pagina html
psw1.send_keys(str+'13')#envio el string
print(str)
clk = driver.find_element_by_xpath("//*[@id='center_column']/div/div/form/div/fieldset/div[2]/div[1]/label").click() 

clk1 = driver.find_element_by_xpath("//*[@id='center_column']/div/div/form/div/fieldset/div[2]/div[4]/button").click() 
