import csv
import pytest
import os
from selenium import webdriver
from pages.login_page import LoginPage

# Ayudante para leer el CSV (buscando la ruta correcta del archivo)
def cargar_datos_csv():
    datos = []
    # Usamos os.path para que no falle la ruta del CSV no importa desde dónde corras el test
    ruta_csv = os.path.join(os.path.dirname(__file__), "usuarios.csv")
    
    with open(ruta_csv, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            error = None if fila["expected_error"] == "None" else fila["expected_error"]
            datos.append((fila["username"], fila["password"], error))
    return datos

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# El test parametrizado usando la estructura POM
@pytest.mark.parametrize("username, password, expected_error", cargar_datos_csv())
def test_login_saucedemo(driver, username, password, expected_error):
    # Inicializamos la página de login pasándole el driver
    login_page = LoginPage(driver)
    
    # Pasos del test usando los métodos del Page Object
    login_page.abrir()
    login_page.ingresar_credenciales(username, password)
    login_page.click_login()
    
    # Validaciones (Aserciones)
    if expected_error is None:
        assert "inventory.html" in driver.current_url
    else:
        assert expected_error in login_page.obtener_texto_error()