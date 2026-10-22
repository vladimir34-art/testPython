import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.auth import InventoryLocators, CartLocators

def test_clear_cart(login_standard):
    driver = login_standard
    wait = WebDriverWait(driver, 10)

    add_buttons = wait.until(EC.presence_of_all_elements_located(InventoryLocators.ADD_TO_CARTS))
    for btn in add_buttons[:2]:
        wait.until(EC.element_to_be_clickable(btn)).click()

    cart_link = wait.until(EC.element_to_be_clickable(InventoryLocators.CART_LINK))
    cart_link.click()

    remove_buttons = wait.until(EC.presence_of_all_elements_located(CartLocators.REMOVE_BUTTONS))
    for btn in remove_buttons:
        wait.until(EC.element_to_be_clickable(btn)).click()

    wait.until(lambda d: len(d.find_elements(*CartLocators.ITEMS)) == 0)

    items = driver.find_elements(*CartLocators.ITEMS)
    assert len(items) == 0
    assert "cart" in driver.current_url