
import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_shop(driver):
    # Открытие страницы
    driver.get("https://www.saucedemo.com/")

    # Данные для заполнения формы авторизации
    form_data = {
        "user-name": "standard_user",
        "password": "secret_sauce",
    }

    # Заполнение формы авторизации
    for field_name, value in form_data.items():
        driver.find_element(By.ID, field_name).send_keys(value)

    # Нажимаем кнопку авторизации
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    button_ids = ["add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-bolt-t-shirt", "add-to-cart-sauce-labs-onesie"]
    for button_id in button_ids:
        item_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, button_id))
        )
        item_button.click()

    # Нажимаем кнопку корзины
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # Нажимаем кнопку Checkout
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    # Заполняем форму

    form_delivery = {
        "first-name": "Анита",
        "last-name": "Коюшева",
        "postal-code": "167000",
    }
    
    for field_id, value in form_delivery.items():
        field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        field.send_keys(value)

    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # Ищем тотал

    total_block = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_block.text

    # Ищем число в тексте 

    numbers = re.findall(r'-?\d+\.?\d*', total_text)
    number_str = numbers[0]
    extracted_number = float(number_str)

    # Сверяем тотал

    expected_number = 58.29
    assert extracted_number == expected_number, f"Ожидалось {expected_number}, получено {extracted_number}"

