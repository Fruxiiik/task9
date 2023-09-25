from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocator as Locators


class CartPage(BasePage):

    def checkout(self):
        self.element_is_visible(Locators.CHECKOUT_BUTTON).click()

