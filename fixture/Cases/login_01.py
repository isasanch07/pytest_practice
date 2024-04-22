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

def test_login_uno():
    global driver
    driver = webdriver.Chrome()
    fl = funciones_login()
    fl.test_login("juanito@gmail.com", "12345", "No customer account found", 2)
    fl.test_login_dos("", "1234", "Please enter your email", 2)
    fl.test_login_tres("Isabel", "12345", "Wrong email", 2)
    fl.test_login_cuatro("admin@yourstore.com", "admin", "Dashboard", 2)


    







   