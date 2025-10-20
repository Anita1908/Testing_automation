
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class CheckoutPage:
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_AMOUNT_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver

    def enter_checkout_details(self, first_name, last_name, postal_code):
        """Ввод контактных данных покупателя."""
        first_name_input: WebElement = self.driver.find_element(*CheckoutPage.FIRST_NAME_FIELD)
        last_name_input: WebElement = self.driver.find_element(*CheckoutPage.LAST_NAME_FIELD)
        postal_code_input: WebElement = self.driver.find_element(*CheckoutPage.POSTAL_CODE_FIELD)
        continue_btn: WebElement = self.driver.find_element(*CheckoutPage.CONTINUE_BUTTON)

        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        postal_code_input.send_keys(postal_code)
        continue_btn.click()

    def get_total_amount(self):
        """Получить итоговую сумму заказа."""
        total_amount_element: WebElement = self.driver.find_element(*CheckoutPage.TOTAL_AMOUNT_LABEL)
        return total_amount_element.text.split(":")[1].strip()

