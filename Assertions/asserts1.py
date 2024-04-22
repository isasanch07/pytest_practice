import pytest
import time
import sys
sys.path.append("..")
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = ""

@pytest.mark.validar_if
def test_numeros():
    a=59
    b=14
    c=4

    #assert a<b, "A es mayor q B"
    assert a == b or a == c, "A es mayor que todos"