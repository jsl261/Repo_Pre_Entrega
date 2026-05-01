from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Clase base que contiene métodos comunes para todas las páginas."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        """Espera a que un elemento sea cliqueable y hace click."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def write(self, locator, text):
        """Espera a que un elemento sea visible y escribe en él."""
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        """Obtiene el texto de un elemento visible."""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_displayed(self, locator):
        """Verifica si un elemento es visible en el DOM."""
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()