import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.auth import InventoryLocators, CartLocators

@pytest.mark.allure(suite="Purchase Flow", severity="critical")
def test_successful_purchase(login_standard):
    driver = login_standard
    wait = WebDriverWait(driver, 30)

    # Закрываем всплывающее окно, если есть
    try:
        ok_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'OK')]")),
            timeout=10
        )
        ok_btn.click()
        print("Всплывающее окно закрыто.")
    except Exception:
        pass

    # Добавляем товар
    add_btn = wait.until(EC.element_to_be_clickable(InventoryLocators.ADD_TO_CARTS))
    add_btn.click()
    print("Товар добавлен.")

    # Проверяем бейдж корзины
    badge = wait.until(EC.visibility_of_element_located(InventoryLocators.CART_BADGE))
    badge_count = int(badge.text)
    assert badge_count > 0, f"Ожидался товар в корзине, но там: {badge_count}"

    # Переходим в корзину
    cart_link = wait.until(EC.element_to_be_clickable(InventoryLocators.CART_LINK))
    cart_link.click()

    assert "cart.html" in driver.current_url, "Не попали на страницу корзины!"

    # Проверяем, что товар есть в списке
    items = wait.until(lambda d: d.find_elements(*CartLocators.ITEMS), message="Товары не появились")
    assert len(items) > 0, "Корзина пуста!"

    # Нажимаем Checkout (ИСПРАВЛЕНИЕ: обычный клик, без JS!)
    checkout_btn = wait.until(
        EC.element_to_be_clickable(CartLocators.CHECKOUT_BUTTON),
        message="Кнопка Checkout не найдена или не кликабельна"
    )
    checkout_btn.click()
    print("Нажата кнопка Checkout.")
