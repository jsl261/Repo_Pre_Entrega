from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    """Página de acceso al sistema Saucedemo."""

    # Selectores
    USER_INPUT = (By.ID, "user-name")
    PASS_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def login(self, username, password):
        """Realiza el flujo completo de login."""
        self.write(self.USER_INPUT, username)
        self.write(self.PASS_INPUT, password)
        self.click(self.LOGIN_BTN)