
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.LoginPage import LoginPage
from page_objects.InventoryPage import InventoryPage
from page_objects.CartPage import CartPage
from page_objects.CheckoutPage import CheckoutPage


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_complete_purchase_flow(driver):
    # Авторизация пользователя
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    # Добавление товаров в корзину
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bolt_tshirt_to_cart()
    inventory_page.add_onesie_to_cart()

    # Переход в корзину
    inventory_page.go_to_cart()

    # Оформление заказа
    cart_page.checkout()

    # Заполнение контактных данных
    checkout_page.enter_checkout_details("John", "Doe", "12345")

    # Проверка итоговой суммы
    total_amount = checkout_page.get_total_amount()
    assert total_amount == "$58.29", f"Итоговая сумма должна быть $58.29, фактическое значение: {total_amount}"

