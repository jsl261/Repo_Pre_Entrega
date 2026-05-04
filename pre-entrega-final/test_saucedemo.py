import pytest
from selenium import webdriver
from funciones_auxiliares import LoginPage, InventoryPage, CartPage

@pytest.fixture
def driver():
    """Configuración y cierre del navegador para cada prueba."""
    opciones = webdriver.ChromeOptions()
    opciones.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opciones)
    
    yield driver  # Retorna el driver a la prueba
    
    driver.quit() # Cierra el navegador al finalizar la prueba

def test_login_exitoso(driver):
    """Verifica que el usuario pueda iniciar sesión y sea redirigido."""
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.iniciar_sesion("standard_user", "secret_sauce")

    # Validación 1: Redirección a la URL correcta
    assert "/inventory.html" in driver.current_url, "Fallo en la redirección."

    # Validación 2: El título de la sección es 'Products'
    inventory_page = InventoryPage(driver)
    assert inventory_page.obtener_titulo_seccion() == "Products", "Título incorrecto."

def test_navegacion_e_inventario(driver):
    """Verifica el título de pestaña, elementos UI y lista un producto."""
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.iniciar_sesion("standard_user", "secret_sauce")

    # Validación 1: Título de la pestaña del navegador
    assert driver.title == "Swag Labs", "El título de la pestaña no es Swag Labs."

    # Validación 2: Elementos importantes de la interfaz (menú y filtros)
    inventory_page = InventoryPage(driver)
    assert inventory_page.validar_elementos_interfaz(), "Faltan elementos de UI."

    # Validación 3: Presencia de productos y captura de datos
    nombre, precio = inventory_page.obtener_datos_primer_producto()
    assert nombre, "No se encontró el nombre del producto."
    assert precio, "No se encontró el precio del producto."
    
    # Se imprime en consola (visible usando pytest -s)
    print(f"\n--- Producto validado: {nombre} | Precio: {precio} ---")

def test_flujo_carrito_compras(driver):
    """Verifica que un producto se agregue correctamente al carrito."""
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.iniciar_sesion("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    
    # Capturamos el nombre para luego buscarlo en el carrito
    nombre_esperado, _ = inventory_page.obtener_datos_primer_producto()

    # Acción: Agregar producto
    inventory_page.agregar_primer_producto_al_carrito()

    # Validación 1: Contador del carrito incrementa a 1
    assert inventory_page.obtener_cantidad_carrito() == "1", "El contador falló."

    # Navegar al carrito
    inventory_page.ir_al_carrito()

    # Validación 2: El producto exacto aparece en el carrito
    cart_page = CartPage(driver)
    producto_existe = cart_page.verificar_producto_en_carrito(nombre_esperado)
    assert producto_existe, f"El producto '{nombre_esperado}' no está en el carrito."

