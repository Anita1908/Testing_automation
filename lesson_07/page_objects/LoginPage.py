
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class LoginPage:
    LOGIN_URL = "https://www.saucedemo.com/"
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        """Открыть страницу авторизации."""
        self.driver.get(LoginPage.LOGIN_URL)

    def login(self, username, password):
        """Осуществить вход в систему."""
        user_input: WebElement = self.driver.find_element(*LoginPage.USERNAME_FIELD)
        pass_input: WebElement = self.driver.find_element(*LoginPage.PASSWORD_FIELD)
        login_btn: WebElement = self.driver.find_element(*LoginPage.LOGIN_BUTTON)

        user_input.send_keys(username)
        pass_input.send_keys(password)
        login_btn.click()

