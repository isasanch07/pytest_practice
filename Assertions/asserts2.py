import pytest
import time
import sys
sys.path.append("..")
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = ""

@pytest.mark.validar_if
def test_validar():
    dato = "Computadora"
    frase = "Probando las frases de aquí"

    assert dato in frase, "El dato {} no está dentro de la frase {}".format(dato, frase)