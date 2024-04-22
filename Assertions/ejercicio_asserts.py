import allure_commons
import pytest
import time
import sys
sys.path.append("..")
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = ""


@pytest.fixture(scope='module')
def setup_login():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    user = driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
    password = driver.find_element(By.XPATH, "//input[@type='password']").send_keys("admin123")
    clic = driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Ingresando al sistema")
    time.sleep(3)
    
def teardown_function():
    print(" \nSaliendo del test")
    driver.close()

@pytest.mark.login
@pytest.mark.usefixtures("setup_login")
def test_uno():
    validar = driver.find_element(By.XPATH, "//h6[contains(.,'Dashboard')]").text
    print("Encontró el elemento {} \n".format(validar))
    assert validar == "Dashboard", "El elemento no es igual"
    
    



