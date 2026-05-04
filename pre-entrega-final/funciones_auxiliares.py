from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Clase base que inicializa el driver y la espera explícita."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

class LoginPage(BasePage):
    """Maneja las interacciones en la página de inicio de sesión."""
    URL = "https://www.saucedemo.com/"

    def abrir(self):
        """Navega a la página de login."""
        self.driver.get(self.URL)

    def iniciar_sesion(self, usuario, contrasena):
        """Ingresa las credenciales y hace clic en el botón de login."""
        # Espera explícita hasta que el campo de usuario sea visible
        campo_usuario = self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        campo_usuario.send_keys(usuario)
        
        self.driver.find_element(By.ID, "password").send_keys(contrasena)
        self.driver.find_element(By.ID, "login-button").click()

class InventoryPage(BasePage):
    """Maneja las interacciones y validaciones en la página de inventario."""
    
    def obtener_titulo_seccion(self):
        """Retorna el texto del título principal de la sección."""
        titulo = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )
        return titulo.text

    def validar_elementos_interfaz(self):
        """Comprueba que el menú hamburguesa y el filtro estén presentes."""
        menu = self.driver.find_elements(By.ID, "react-burger-menu-btn")
        filtros = self.driver.find_elements(By.CLASS_NAME, "product_sort_container")
        # Retorna True si ambos elementos existen en el DOM
        return len(menu) > 0 and len(filtros) > 0

    def obtener_datos_primer_producto(self):
        """Retorna el nombre y precio del primer producto en la lista."""
        nombre = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
        ).text
        precio = self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text
        return nombre, precio

    def agregar_primer_producto_al_carrito(self):
        """Hace clic en el primer botón de 'Add to cart' disponible."""
        btn_agregar = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//button[text()='Add to cart'])[1]"))
        )
        btn_agregar.click()

    def obtener_cantidad_carrito(self):
        """Retorna el número de ítems indicados en el icono del carrito."""
        badge = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        return badge.text

    def ir_al_carrito(self):
        """Navega a la página del carrito de compras."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

class CartPage(BasePage):
    """Maneja las interacciones en la página del carrito."""
    
    def verificar_producto_en_carrito(self, nombre_producto):
        """Comprueba si un producto específico está en el listado del carrito."""
        nombres_carrito = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))
        )
        for elemento in nombres_carrito:
            if elemento.text == nombre_producto:
                return True
        return False
