import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.auth import InventoryLocators, CartLocators, CheckoutLocators

def test_successful_purchase(login_standard):
    driver = login_standard
    wait = WebDriverWait(driver, 30)

    try:
        ok_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'OK')]")), timeout=5)
        ok_btn.click()
        print("Всплывающее окно 'Смените пароль' закрыто.")
    except Exception:
        pass 

    add_btn = wait.until(EC.element_to_be_clickable(InventoryLocators.ADD_TO_CARTS))
    add_btn.click()
    print("Товар добавлен (один клик).")

    badge = wait.until(EC.visibility_of_element_located(InventoryLocators.CART_BADGE))
    badge_count = int(badge.text)
    assert badge_count > 0, f"Ожидалось хотя бы 1 товар в корзине, но там: {badge_count}"
    print(f"В корзине товаров: {badge_count}")

    cart_link = wait.until(EC.element_to_be_clickable(InventoryLocators.CART_LINK))
    cart_link.click()

    print("Current URL:", driver.current_url)
    assert "cart.html" in driver.current_url, "Не попали на страницу корзины!"

    items = wait.until(lambda d: d.find_elements(*CartLocators.ITEMS), message="Товары не появились в DOM корзины")
    assert len(items) > 0, "Корзина пуста! Товар не добавился в список."
    print(f"В корзине найдено строк товаров: {len(items)}")

    checkout_btn = wait.until(
        EC.presence_of_element_located(CartLocators.CHECKOUT_BUTTON),
        message="Кнопка Checkout не найдена"
    )
    driver.execute_script("arguments.click();", checkout_btn)
    print("Кнопка Checkout нажата.")

    first_name_input = wait.until(EC.visibility_of_element_located(CheckoutLocators.FIRST_NAME))
    first_name_input.clear()
    first_name_input.send_keys("Vladimir")

    last_name_input = driver.find_element(*CheckoutLocators.LAST_NAME)
    last_name_input.clear()
    last_name_input.send_keys("Volnykh")

    postal_code_input = driver.find_element(*CheckoutLocators.POSTAL_CODE)
    postal_code_input.clear()
    postal_code_input.send_keys("197601")

    continue_btn = wait.until(EC.element_to_be_clickable(CheckoutLocators.CONTINUE_BUTTON))
    continue_btn.click()

    wait = WebDriverWait(driver, 45) 
    wait.until(lambda d: "checkout-summary" in d.current_url)

    finish_btn = wait.until(EC.element_to_be_clickable(CheckoutLocators.FINISH_BUTTON))
    finish_btn.click()

    header = wait.until(EC.visibility_of_element_located(CheckoutLocators.COMPLETE_HEADER))
    assert "THANKS FOR YOUR ORDER!" in header.text, f"Ожидался заголовок с 'THANKS FOR YOUR ORDER!', но получили: {header.text}"

    print("Тест успешно пройден!")
