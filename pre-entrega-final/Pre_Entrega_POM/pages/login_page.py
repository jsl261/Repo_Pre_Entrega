from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        
        # Locators (Centralizados acá)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_container = (By.CSS_SELECTOR, "[data-test='error']")

    def abrir(self):
        self.driver.get(self.url)

    def ingresar_credenciales(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def obtener_texto_error(self):
        return self.driver.find_element(*self.error_container).text