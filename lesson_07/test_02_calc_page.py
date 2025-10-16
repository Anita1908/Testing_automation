
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.calculator_page import CalculatorPage


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculate_sum(driver):
    calc_page = CalculatorPage(driver)
    calc_page.open()
    calc_page.set_delay("45")
    calc_page.calculate("7+8=")

    # Ждем 45 секунд и проверяем результат
    result = calc_page.get_result()
    assert result == "15", f"Результат вычисления некорректен. Получили: {result}, ожидали: 15."

