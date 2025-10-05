
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def is_visible(element):
    """Проверяем видимость элемента"""
    try:
        return element.is_displayed()
    except StaleElementReferenceException:
        return False

# Создаем объект веб-драйвера Chrome
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    # Ждем полного завершения загрузки страницы
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))  # Подождать основную загрузку страницы
    
    # Периодически проверяем наличие и видимость третьего изображения
    while True:
        all_images = driver.find_elements(By.TAG_NAME, 'img')
        visible_images = [img for img in all_images if is_visible(img)]
        
        if len(visible_images) >= 3:
            break
    
    # Теперь точно уверены, что третья картинка доступна
    third_image = visible_images[2]
    third_image_src = third_image.get_attribute('src')
    
    # Выводим значение в консоль
    print(f"Значение атрибута src третьей картинки: {third_image_src}")

except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    # Закрываем браузер
    driver.quit()

    