
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запускаем браузер Chrome
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get('http://uitestingplayground.com/textinput')
    
    # Ждем пока появится поле ввода
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#newButtonName')) 
    )
    
    # Вводим текст "SkyPro" в поле
    input_field.send_keys('SkyPro')
    
    # Ожидаем, пока кнопка станет кликабельной 
    submit_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn'))  
    )
    
    # Нажимаем на кнопку
    submit_button.click()
    
    # Подтверждаем изменение имени кнопки (текст на кнопке стал "SkyPro")
    updated_button = WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'button[id=updatingButton]'), "SkyPro")  
    )
    
    # Проверяем новый текст кнопки
    new_button_text = submit_button.text.strip()
    
    # Выводим текст кнопки в консоль
    print(new_button_text)

finally:
    # Закрываем браузер
    driver.quit()

