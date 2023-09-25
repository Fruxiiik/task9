from selenium.webdriver.common.by import By


class CartInfoPageLocator:

    FIRST_NAME = (By.CSS_SELECTOR, '#first-name')
    LAST_NAME = (By.CSS_SELECTOR, '#last-name')
    POSTAL_CODE = (By.CSS_SELECTOR, '#postal-code')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '#continue')
