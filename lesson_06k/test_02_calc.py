
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calculator():
    # Открытие страницы в браузере
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    try:
        # Установка задержки расчета калькулятора
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys('45')

        # Кнопки калькулятора теперь ищем по тексту внутри span
        button_7 = driver.find_element(By.XPATH, "//span[text()='7']")  # Поиск кнопки с текстом "7"
        button_plus = driver.find_element(By.XPATH, "//span[text()='+']")  # Поиск кнопки "+"
        button_8 = driver.find_element(By.XPATH, "//span[text()='8']")  # Поиск кнопки с текстом "8"
        button_equals = driver.find_element(By.XPATH, "//span[text()='=']")  # Поиск кнопки "="

        # Последовательность действий
        button_7.click()
        button_plus.click()
        button_8.click()
        button_equals.click()

        # Ищем элемент вывода результата
        text_block = driver.find_element(By.CLASS_NAME, "screen")
        initial_text = text_block.text

        # Используем WebDriverWait для ожидания результата
        # Ожидаем изменения поля результата (т.к. равен полю ввода)
        wait = WebDriverWait(driver, 50)
        wait.until(
            lambda driver: text_block.text != initial_text
        )
        result_text = text_block.text    

        # Проверка результата
        assert result_text.strip() == "15", f"Результат неверный: {result_text}"

        print(f"Результат верный: {result_text}")    

    finally:
        # Закрыть браузер
        driver.quit()

if __name__ == "__main__":
    test_calculator()
    
    