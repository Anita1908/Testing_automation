
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class CartPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        """Перейти к процессу оформления заказа."""
        checkout_btn: WebElement = self.driver.find_element(*CartPage.CHECKOUT_BUTTON)
        checkout_btn.click()

