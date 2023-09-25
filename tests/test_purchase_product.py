from pages.cart_page import CartPage
from pages.cart_information_page import CartInformationPage
from pages.cart_final_page import CartFinalPage
from pages.main_page import MainPage
from pages.form_page import FormPage
import pytest
import random


class TestPurchaseProducts:

    products = [
        {'name': 'Sauce Labs Backpack', 'price': '$29.99', 'button_name': "sauce-labs-bike-light"},
        {'name': 'Sauce Labs Bolt T-Shirt', 'price': '$15.99', 'button_name': "sauce-labs-bolt-t-shirt"},
        {'name': 'Sauce Labs Onesie', 'price': '$7.99', 'button_name': "sauce-labs-onesie"},
        {'name': 'Sauce Labs Bike Light', 'price': '$9.99', 'button_name': "sauce-labs-bike-light"},
        {'name': 'Sauce Labs Fleece Jacket', 'price': '$49.99', 'button_name': "sauce-labs-fleece-jacket"},
        {'name': 'Test.allTheThings() T-Shirt (Red)', 'price': '$15.99', 'button_name': "test.allthethings()-t-shirt-(red)"}

    ]

    @pytest.mark.parametrize("product", products)
    def test_purchase_products(self, driver, product):
        username = 'standard_user'
        form_page = FormPage(driver, "https://www.saucedemo.com/")
        form_page.open()
        form_page.login(username)

        main_page = MainPage(driver, "https://www.saucedemo.com/inventory.html")
        main_page.add_to_cart(product['button_name'])
        main_page.link_to_cart()

        cart_page = CartPage(driver, "https://www.saucedemo.com/cart.html")
        cart_page.checkout()

        cart_info_page = CartInformationPage(driver, "https://www.saucedemo.com/checkout-step-one.html")
        cart_info_page.fill_info_checkout()

        cart_final_page = CartFinalPage(driver, "https://www.saucedemo.com/checkout-step-two.html")
        cart_final_page.finish_checkout()

        assert "checkout-complete.html" in driver.current_url, f"Purchase of {product['name']} failed"

    def test_cart_counter(self, driver):
        username = 'standard_user'
        form_page = FormPage(driver, "https://www.saucedemo.com/")
        form_page.open()
        form_page.login(username)

        random_index_1 = random.randint(0, len(self.products) - 1)
        random_product_1 = self.products[random_index_1]

        while True:
            random_index_2 = random.randint(0, len(self.products) - 1)
            if random_index_2 != random_index_1:
                break
        random_product_2 = self.products[random_index_2]

        main_page = MainPage(driver, "https://www.saucedemo.com/inventory.html")
        main_page.add_to_cart(random_product_1['button_name'])
        cart_counter = main_page.count_products_in_cart()

        assert int(cart_counter) == 1, 'The first product was not added to the cart'
        main_page.add_to_cart(random_product_2['button_name'])
        new_cart_counter = main_page.count_products_in_cart()

        assert int(new_cart_counter) == int(cart_counter) + 1, 'The second product was not added to the cart'

        main_page.remove_from_cart(random_product_2['button_name'])
        final_cart_counter = main_page.count_products_in_cart()

        assert int(new_cart_counter) - 1 == int(final_cart_counter), 'The product was not removed from the cart'















        












