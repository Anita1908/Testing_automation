
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time  # Импортируем модуль для добавления задержки

# Подготовка драйвера и настроек
service = FirefoxService(GeckoDriverManager().install())
options = Options()
driver = webdriver.Firefox(service=service, options=options)

try:
    # Перейти на сайт
    driver.get('http://the-internet.herokuapp.com/login')

    # Небольшая пауза для полной загрузки страницы (задержка в 2 секунды)
    time.sleep(2)

    # Найти элементы формы и заполнить их
    username_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')

    username_input.send_keys('tomsmith')       # Вводим логин
    password_input.send_keys('SuperSecretPassword!')  # Вводим пароль

    # Пауза после клика на кнопку (чтобы дождаться появления сообщений)
    time.sleep(2)

    # Нажать кнопку входа
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()

    # Получаем текст зеленого уведомления
    success_message = driver.find_element(By.CLASS_NAME, 'flash.success').text.strip()
    print(f'Сообщение успеха: {success_message}')

finally:
    # Закрываем браузер
    driver.quit()

