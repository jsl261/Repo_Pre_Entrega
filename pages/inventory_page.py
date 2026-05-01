from selenium.webdriver.common.by import By
from .base_page import BasePage


class InventoryPage(BasePage):
    """Página de inventario y carrito de compras."""

    # Selectores de Interfaz
    TITLE = (By.CLASS_NAME, "title")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    FILTER_SELECT = (By.CLASS_NAME, "product_sort_container")

    # Selectores de Productos
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    FIRST_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    FIRST_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    # Selectores de Carrito
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) button")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def get_first_product_info(self):
        """Retorna una tupla con (nombre, precio) del primer producto."""
        name = self.get_text(self.FIRST_ITEM_NAME)
        price = self.get_text(self.FIRST_ITEM_PRICE)
        return name, price

    def add_first_product_to_cart(self):
        """Agrega el primer ítem de la lista al carrito."""
        self.click(self.ADD_TO_CART_BTN)

    def go_to_cart(self):
        """Navega a la página del carrito."""
        self.click(self.CART_LINK)