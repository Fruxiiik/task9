from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocator as Locators


class MainPage(BasePage):

    def logout(self):
        self.element_is_visible(Locators.MENU_BUTTON).click()
        self.element_is_visible(Locators.LOGOUT_BUTTON).click()

    def add_to_cart(self, button_name):
        self.element_is_visible(Locators.ADD_TO_CART_BUTTON(button_name)).click()

    def remove_from_cart(self, button_name):
        self.element_is_visible(Locators.REMOVE_FROM_CART_BUTTON(button_name)).click()

    def link_to_cart(self):
        self.element_is_visible(Locators.CART_LINK).click()

    def count_products_in_cart(self):
        cart_counter = self.element_is_visible(Locators.CART_COUNTER).text
        return cart_counter

    def select_sorting(self, sorting_kind):
        self.element_is_visible(Locators.SORT_DROPDOWN).click()
        self.element_is_visible(Locators.SORT_OPTION(sorting_kind)).click()

    def get_product_order(self):
        product_order = self.elements_are_visible(Locators.PRODUCT_ELEMENTS)
        product_order_text = [element.text for element in product_order]
        return product_order_text

    def get_product_order_prices(self):
        product_order_prices = self.elements_are_visible(Locators.PRODUCT_PRICES)
        product_order_prices_text = [float(item.text.strip("$")) for item in product_order_prices]
        return product_order_prices_text










