import pytest
import time
import sys
sys.path.append("..")
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = ""

@pytest.mark.validar_if
def test_validar_if():
    nom1 = "Isa"
    nom2 = "Isa"
    assert nom1==nom2,  "Los nombres son distintos"
