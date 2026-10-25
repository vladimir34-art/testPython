import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.auth import InventoryLocators, CartLocators

class TestCartOperations:
    @pytest.mark.allure(title="TC-002: Очистка корзины", severity="critical")
    def test_clear_cart(self, login_standard):
        driver = login_standard
        wait = WebDriverWait(driver, 30)

        # 1. Добавляем 2 товара
        add_buttons = wait.until(
            lambda d: d.find_elements(*InventoryLocators.ADD_TO_CARTS),
            message="Не найдены кнопки Add to Cart"
        )
        assert len(add_buttons) >= 2, "На странице меньше 2 товаров!"

        for i in range(2):
            add_buttons[i].click()
        print("Два товара добавлены.")

        # 2. Проверяем бейдж корзины
        badge = wait.until(EC.visibility_of_element_located(InventoryLocators.CART_BADGE))
        badge_count = int(badge.text)
        assert badge_count >= 2, f"В корзине меньше 2 товаров: {badge_count}"

        # 3. Переходим в корзину
        cart_link = wait.until(EC.element_to_be_clickable(InventoryLocators.CART_LINK))
        cart_link.click()

        # Небольшая пауза, чтобы страница точно обновилась
        driver.implicitly_wait(1)

        # 4. Удаляем товары по одному
        while True:
            remove_buttons = driver.find_elements(*CartLocators.REMOVE_BUTTONS)
            if not remove_buttons:
                break  # Кнопок нет — корзина пуста

            first_btn = remove_buttons[0]
            # Самый надёжный способ: клик через JS
            driver.execute_script("arguments[0].click();", first_btn)
            print("Нажата кнопка Remove.")

            # Ждём, пока количество товаров уменьшится
            wait.until(
                lambda d: len(d.find_elements(*CartLocators.ITEMS)) < len(remove_buttons),
                message="Количество товаров не уменьшилось после удаления"
            )

        print("Корзина очищена.")

               # 5. Финальная проверка: ждём, пока корзина станет пустой
        def is_cart_empty(driver):
            items = driver.find_elements(*CartLocators.ITEMS)
            return len(items) == 0

        wait.until(is_cart_empty, message="Корзина не стала пустой за отведённое время")
        print("Корзина точно пуста — тест пройден.")


