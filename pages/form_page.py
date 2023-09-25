from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocator as Locators


class FormPage(BasePage):

    def login(self, user_name):
        password = 'secret_sauce'

        self.element_is_visible(Locators.USERNAME).send_keys(user_name)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.LOGIN_BUTTON).click()

    def find_error(self):
        error_message = self.element_is_visible(Locators.ERROR_MESSAGE)
        return error_message



