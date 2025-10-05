
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем браузер Chrome
driver = webdriver.Chrome()

try:
    # Переходим на нужную страницу
    driver.get("http://uitestingplayground.com/ajax")
    
    # Ждем появления кнопки
    button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    
    # Кликаем на кнопку
    button.click()
    
    # Увеличили время ожидания появления зеленого блока
    result_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.bg-success'))
    )
    
    # Получаем текст из результата
    result_text = result_element.text.strip()
    
    print(result_text)

finally:
    # Закрываем браузер
    driver.quit()

