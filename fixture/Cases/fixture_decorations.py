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

#Si voy a usar distintos setups debo colocar el decorador @pytest.fixture, de lo contrario no me va a aparecer

#Es como dar un ID para poderlo seleccionar
@pytest.fixture(scope='module')
def setup_login_uno():
    print("comenzando login del sistema")
    yield
    print("Saliendo del sistema, todo ok \n")

@pytest.fixture(scope='module')
def setup_login_dos():
    print("comenzando login 2 del sistema")
    yield
    print("Saliendo del sistema 2, todo ok\n")


def test_uno(setup_login_uno):
    print("Comenzando test 1")

def test_dos(setup_login_dos):
    print("Segunda prueba")

#Otra forma de llamarlo:
@pytest.mark.usefixtures("setup_login_dos")
def test_tres():
    print("prueba 3 del 2do setup")