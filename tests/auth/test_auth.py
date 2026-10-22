import pytest
from locators.auth import AuthLocators

def test_unsuccessful_login(driver):
    driver.get("https://www.saucedemo.com/")
    
    username_input = driver.find_element(*AuthLocators.USERNAME_FIELD)
    password_input = driver.find_element(*AuthLocators.PASSWORD_FIELD)
    login_btn = driver.find_element(*AuthLocators.LOGIN_BUTTON)

    username_input.send_keys("wrong_user")
    password_input.send_keys("wrong_password")
    login_btn.click()

    error_msg = driver.find_element(*AuthLocators.ERROR_MESSAGE)
    assert "Epic sadface" in error_msg.text
