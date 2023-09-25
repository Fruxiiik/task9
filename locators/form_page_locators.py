from selenium.webdriver.common.by import By


class FormPageLocator:

    USERNAME = (By.CSS_SELECTOR, '#user-name')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '#logout_sidebar_link')
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
