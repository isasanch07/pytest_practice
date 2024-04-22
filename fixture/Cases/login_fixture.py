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
from Funciones.funcion import funciones
from page_login import funciones_login

def setup_function():
    print("Comienzo de cada case ")
    driver = webdriver.Chrome()
    driver.get("https://admin-demo.nopcommerce.com/login")
    driver.maximize_window()
    time.sleep(2)
    email = driver.find_element(By.XPATH, "//input[contains(@id,'Email')]")
    email.clear()
    email.send_keys("admin@yourstore.com")
    password = driver.find_element(By.XPATH, "//input[contains(@id,'Password')]")
    password.clear()
    password.send_keys("admin")
    driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
    time.sleep(2)


def teardown_function():
    print("fin de cada test \n")
    driver=webdriver.Chrome()
    driver.close()

def test_uno():
    print("Test uno\n")
    driver = webdriver.Chrome()
    #driver.find_element(By.XPATH, "//*[@id='nopSideBarPusher']").click()
    driver.find_element(By.XPATH, "(//p[contains(.,'Catalog')])[1]").click()
    driver.find_element(By.XPATH, "(//p[contains(.,'Products')])[1]").click()
    driver.find_element(By.XPATH, "//div[@data-hideattribute='ProductListPage.HideSearchBlock']").click()
    time.sleep(2)
    
    

def test_dos():
    print("Test dos\n")




