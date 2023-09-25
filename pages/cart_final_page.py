from pages.base_page import BasePage
from locators.cart_final_page_locators import CartFinalPageLocator as Locators


class CartFinalPage(BasePage):

    def finish_checkout(self):
        self.element_is_visible(Locators.FINISH_BUTTON).click()