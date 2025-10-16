
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    DELAY_INPUT = (By.ID, "delay")
    RESULT_OUTPUT = (By.ID, "result")
    BUTTON_7 = (By.XPATH, "//span[@data-test-id='seven-button']")
    BUTTON_PLUS = (By.XPATH, "//span[@data-test-id='plus-button']")
    BUTTON_8 = (By.XPATH, "//span[@data-test-id='eight-button']")
    BUTTON_EQUALS = (By.XPATH, "//span[@data-test-id='equals-button']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Открыть страницу калькулятора."""
        self.driver.get(CalculatorPage.URL)

    def set_delay(self, delay_value):
        """Установить задержку перед отображением результата вычисления."""
        delay_input: WebElement = self.driver.find_element(*CalculatorPage.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(delay_value)

    def press_button(self, button_xpath):
        """Нажать кнопку калькулятора по заданному XPath."""
        button: WebElement = self.driver.find_element(By.XPATH, button_xpath)
        button.click()

    def calculate(self, expression):
        """Выполнить расчет выражения на калькуляторе."""
        buttons = [
            CalculatorPage.BUTTON_7,
            CalculatorPage.BUTTON_PLUS,
            CalculatorPage.BUTTON_8,
            CalculatorPage.BUTTON_EQUALS
        ]
        for button in buttons[:len(expression)]:
            self.press_button(button[1])

    def get_result(self):
        """Получить результат расчета."""
        result_output: WebElement = WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element(CalculatorPage.RESULT_OUTPUT, "15")
        )
        return result_output.text.strip()

