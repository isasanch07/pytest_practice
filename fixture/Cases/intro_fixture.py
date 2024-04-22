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

def setup_function(function):
    print("Comienzo de cada case ")

def teardown_function(function):
    print("fin de cada test \n")

def test_uno():
    print("Test uno\n")

def test_dos():
    print("Test dos\n")

def test_tres():
    print("Test tres\n")

def test_cuatro():
    print("Test cuatro\n")