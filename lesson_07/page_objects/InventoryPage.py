
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class InventoryPage:
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TO_CART_BOLT_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_TO_CART_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        """Добавить рюкзак в корзину."""
        backpack_add_btn: WebElement = self.driver.find_element(*InventoryPage.ADD_TO_CART_BACKPACK)
        backpack_add_btn.click()

    def add_bolt_tshirt_to_cart(self):
        """Добавить футболку в корзину."""
        tshirt_add_btn: WebElement = self.driver.find_element(*InventoryPage.ADD_TO_CART_BOLT_TSHIRT)
        tshirt_add_btn.click()

    def add_onesie_to_cart(self):
        """Добавить детский костюмчик в корзину."""
        onesie_add_btn: WebElement = self.driver.find_element(*InventoryPage.ADD_TO_CART_ONESIE)
        onesie_add_btn.click()

    def go_to_cart(self):
        """Перейти в корзину покупок."""
        cart_icon: WebElement = self.driver.find_element(*InventoryPage.CART_ICON)
        cart_icon.click()

