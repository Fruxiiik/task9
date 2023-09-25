from pages.base_page import BasePage
from locators.cart_information_page_locators import CartInfoPageLocator as Locators
from generator.generator import generated_person


class CartInformationPage(BasePage):

    def fill_info_checkout(self):
        person = generated_person()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(Locators.POSTAL_CODE).send_keys(person.postal_code)
        self.element_is_visible(Locators.CONTINUE_BUTTON).click()
