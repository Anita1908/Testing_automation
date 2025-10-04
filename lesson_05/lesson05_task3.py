
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Настройка драйвера для Firefox
options = Options()
service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

try:
    # Переход на целевую страницу
    driver.get('http://the-internet.herokuapp.com/inputs')

    # Поиск input-поля по имени атрибута
    input_field = driver.find_element(By.TAG_NAME, 'input')

    # Ввод текста "Sky"
    input_field.send_keys('Sky')

    # Очистка поля
    input_field.clear()

    # Ввод нового текста "Pro"
    input_field.send_keys('Pro')

finally:
    # Закрытие браузера
    driver.quit()

    