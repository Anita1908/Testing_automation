
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Создаем сервис для Chrome Driver
service = Service(ChromeDriverManager().install())

# Создаем объект WebDriver с указанием сервиса
driver = webdriver.Chrome(service=service)

# Остальной код для взаимодействия с браузером
# Например, открытие страницы
driver.get("https://www.google.com/")

# Ждем загрузки страницы
WebDriverWait(driver, 10).until(EC.title_is("Google"))

# Другие действия с браузером...

# Закрываем браузер
driver.quit()

