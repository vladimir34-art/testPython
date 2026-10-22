from selenium.webdriver.common.by import By

class AuthLocators:
    LOGIN_BUTTON = (By.ID, "login-button")
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

class InventoryLocators:
    ADD_TO_CARTS = (By.CSS_SELECTOR, ".btn_primary.btn_inventory")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_container")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge") 

class CartLocators:
    ITEMS = (By.CLASS_NAME, "cart_item")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, ".cart_button")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".checkout_button")

class CheckoutLocators:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".btn_primary.cart_button")
    FINISH_BUTTON = (By.CSS_SELECTOR, ".btn_action.cart_button")
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")
    COMPLETE_TEXT = (By.CSS_SELECTOR, ".complete-text")

