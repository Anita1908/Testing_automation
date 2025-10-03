
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options  # Импортируем класс Options

# Настроим опции для обхода ошибок сертификатов
options = Options()
options.add_argument("--ignore-certificate-errors")  # Игнорируем ошибки сертификатов
options.add_argument("--allow-insecure-localhost")  # Разрешаем небезопасные подключения к localhost

# Устанавливаем драйвер и запускаем браузер с заданными опциями
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)  # Передаем опции при создании драйвера

try:
    # Открываем страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Ждем появления кнопки (ожидаем появление элемента с текстом "Button")
    button_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Button')]"))
    )

    # Кликаем по кнопке
    button_element.click()

    print("Кнопка нажата успешно!")

finally:
    # Закрываем браузер
    driver.quit()

    