import pytest
import time
import sys
sys.path.append("..")
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#Doble validación

@pytest.mark.validar_if
def test_validar():
    a=25
    b=25
    if(a==b):
        print("\n Los datos son iguales")
        assert True
    else:
        assert a==b, "Los datos son distintos"