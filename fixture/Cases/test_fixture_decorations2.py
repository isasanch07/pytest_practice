#NO FUNCIONA

import pytest
import time
import sys
sys.path.append("..")
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from Funciones.funcion import funciones



@pytest.fixture(scope='module')
def setup_login():
    driver = webdriver.Chrome()
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    email = driver.find_element(By.XPATH, "//input[contains(@id,'Email')]")
    email.clear()
    email.send_keys("admin@yourstore.com")
    password = driver.find_element(By.XPATH, "//input[contains(@id,'Password')]")
    password.clear()
    password.send_keys("admin")
    driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Log in')]").click()
    time.sleep(2)
    print("Ingresando al sistema")
    yield
    ("Cerrando el login")
    driver.close()

@pytest.fixture(scope='module')
def setup_login_2():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    email = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
    email.clear()
    email.send_keys("standard_user")
    password = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
    password.clear()
    password.send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]").click()
    time.sleep(2)
    print("Ingresando al sistema dos")
    yield
    ("Cerrando el login 2")
    driver.close()

@pytest.mark.usefixtures("setup_login")
def test_login():
    driver = webdriver.Chrome()
    f=funciones()
    f.cliquear("(//p[contains(.,'Customers')])[1]")
    print("Probando test 1")
    
    time.sleep(2)
    

