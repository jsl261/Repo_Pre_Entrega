import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def driver():
    """Fixture para inicializar y cerrar el navegador."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_full_workflow(driver):
    """Prueba integral: Login -> Navegación -> Carrito."""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # 1. Automatización de Login
    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # Validaciones de Login
    assert "/inventory.html" in driver.current_url
    assert inventory_page.get_text(inventory_page.TITLE) == "Products"

    # 2. Caso de Prueba de Navegación
    assert inventory_page.is_displayed(inventory_page.MENU_BTN)
    assert inventory_page.is_displayed(inventory_page.FILTER_SELECT)

    # Validar productos y listar el primero
    name, price = inventory_page.get_first_product_info()
    print(f"\n[QA Info] Primer Producto: {name} | Precio: {price}")
    assert len(name) > 0

    # 3. Caso de Prueba de Carrito
    inventory_page.add_first_product_to_cart()
    assert inventory_page.get_text(inventory_page.CART_BADGE) == "1"

    inventory_page.go_to_cart()
    assert "/cart.html" in driver.current_url
    assert inventory_page.get_text(inventory_page.FIRST_ITEM_NAME) == name