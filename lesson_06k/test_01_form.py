
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_submission(driver):
    # Открытие страницы
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Данные для заполнения формы
    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    # Заполнение формы
    for field_name, value in form_data.items():
        driver.find_element(By.NAME, field_name).send_keys(value)

    # Нажимаем кнопку Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Явное ожидание, пока поле Zip code получит класс "alert-danger"
    zip_code_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    assert "alert-danger" in zip_code_field.get_attribute("class"), "Поле Zip code не подсвечено красным"

    # Явное ожидание, пока остальные поля получат класс "alert-success"
    
    for field_name, value in form_data.items():
        el = driver.find_element(By.ID, field_name)
        if el != zip_code_field:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, field_name))
            )
            assert "alert-success" in el.get_attribute("class"), f"Поле {el.get_attribute('id')} не подсвечено зеленым"

            
