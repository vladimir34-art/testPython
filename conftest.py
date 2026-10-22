import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators.auth import AuthLocators, InventoryLocators, CartLocators, CheckoutLocators

@pytest.fixture(scope="function")
def login_standard():
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")

    # Логинимся
    driver.find_element(*AuthLocators.USERNAME_FIELD).send_keys("standard_user")
    driver.find_element(*AuthLocators.PASSWORD_FIELD).send_keys("secret_sauce")
    driver.find_element(*AuthLocators.LOGIN_BUTTON).click()

    yield driver
    driver.quit()