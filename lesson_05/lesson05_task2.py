
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запускаем браузер
driver = webdriver.Chrome()

try:
    # Открываем тестовую страницу
    driver.get("http://uitestingplayground.com/dynamicid")
    
    # Ждем немного, пока страница загрузится
    time.sleep(2)
    
    # Находим кнопку по классу CSS-класса кнопки (например, btn)
    button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    
    # Нажимаем на кнопку
    button.click()
    
    print("Кнопка нажата успешно!")

finally:
    # Закрываем браузер
    driver.quit()

