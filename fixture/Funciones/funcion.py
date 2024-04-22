import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select




timeout = 3

class funciones():

    def __init__(self):
        self.driver = webdriver.Chrome()

    
    def cliquear (xpath):
        driver = webdriver.Chrome()
        clic = driver.find_element(By.XPATH, xpath)
        clic.click()
        time.sleep(2)