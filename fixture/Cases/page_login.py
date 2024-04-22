import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from Funciones.funcion import funciones



timeout = 3

class funciones_login():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def test_login(self, email, password, message, segundos):
        global driver
        driver = webdriver.Chrome()
        f=funciones()
        f.navegador("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 2)
        f.rellenar_campos("//input[contains(@id,'Email')]", email, 2)
        f.rellenar_campos("//input[contains(@id,'Password')]", password, 2)
        f.cliquear("//button[@type='submit'][contains(.,'Log in')]", 2)
        error1 = f.finding_elements("//li[contains(.,'No customer account found')]")
        error1 = error1.text
        if (error1 == message):
            print("La prueba se ha ejecutado EXITOSAMENTE")
        else: 
            print("La prueba ha FALLADO")
        time.sleep(segundos)
        driver.close()

    def test_login_dos(self, email, password, message, segundos):
        global driver
        driver = webdriver.Chrome()
        f=funciones()
        f.navegador("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 2)
        f.rellenar_campos("//input[contains(@id,'Email')]", email, 2)
        f.rellenar_campos("//input[contains(@id,'Password')]", password, 2)
        f.cliquear("//button[@type='submit'][contains(.,'Log in')]", 2)
        error2 = f.finding_elements("//span[contains(@id,'Email-error')]")
        error2 = error2.text
        if (error2 == message):
            print("La prueba se ha ejecutado EXITOSAMENTE")
        else: 
            print("La prueba ha FALLADO")
        time.sleep(segundos)
        driver.close()

    def test_login_tres(self, email, password, message, segundos):
        global driver
        driver = webdriver.Chrome()
        f=funciones()
        f.navegador("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 2)
        f.rellenar_campos("//input[contains(@id,'Email')]", email, 2)
        f.rellenar_campos("//input[contains(@id,'Password')]", password, 2)
        f.cliquear("//button[@type='submit'][contains(.,'Log in')]", 2)
        error3 = f.finding_elements("//span[contains(@id,'Email-error')]")
        error3 = error3.text
        if (error3 == message):
            print("La prueba se ha ejecutado EXITOSAMENTE")
        else: 
            print("La prueba ha FALLADO")
        time.sleep(segundos)
        driver.close()

    def test_login_cuatro(self, email, password, message, segundos):
        global driver
        driver = webdriver.Chrome()
        f=funciones()
        f.navegador("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 2)
        f.rellenar_campos("//input[contains(@id,'Email')]", email, 2)
        f.rellenar_campos("//input[contains(@id,'Password')]", password, 2)
        f.cliquear("//button[@type='submit'][contains(.,'Log in')]", 2)
        login = f.finding_elements("//h1[contains(.,'Dashboard')]")
        login = login.text
        if (login == message):
            print("se ha iniciado correctamente")
        else:
            print("ha fallado")
        time.sleep(segundos)
        driver.close()