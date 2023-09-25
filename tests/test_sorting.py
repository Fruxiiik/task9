from pages.main_page import MainPage
from pages.form_page import FormPage


class TestPurchaseProducts:

    def test_sorting_a_to_z(self, driver):
        sorting_kind = 'Name (A to Z)'

        username = 'standard_user'
        form_page = FormPage(driver, "https://www.saucedemo.com/")
        form_page.open()
        form_page.login(username)

        main_page = MainPage(driver, "https://www.saucedemo.com/inventory.html")
        original_product_name = main_page.get_product_order()

        main_page.select_sorting(sorting_kind)

        sorted_product_name = main_page.get_product_order()

        expected_sorted_name = sorted(original_product_name)
        assert sorted_product_name == expected_sorted_name, f'Sorting {sorting_kind} failed'

    def test_sorting_z_to_a(self, driver):
        sorting_kind = 'Name (Z to A)'

        username = 'standard_user'
        form_page = FormPage(driver, "https://www.saucedemo.com/")
        form_page.open()
        form_page.login(username)

        main_page = MainPage(driver, "https://www.saucedemo.com/inventory.html")
        original_product_name = main_page.get_product_order()

        main_page.select_sorting(sorting_kind)

        sorted_product_name = main_page.get_product_order()

        expected_sorted_name = sorted(original_product_name, reverse=True)
        assert sorted_product_name == expected_sorted_name, f'Sorting {sorting_kind} failed'

    def test_sorting_low_to_high(self, driver):
        sorting_kind = 'Price (low to high)'

        username = 'standard_user'
        form_page = FormPage(driver, "https://www.saucedemo.com/")
        form_page.open()
        form_page.login(username)

        main_page = MainPage(driver, "https://www.saucedemo.com/inventory.html")
        original_product_price = main_page.get_product_order_prices()

        main_page.select_sorting(sorting_kind)

        sorted_product_price = main_page.get_product_order_prices()

        expected_sorted_price = sorted(original_product_price)
        assert sorted_product_price == expected_sorted_price, f'Sorting {sorting_kind} failed'

    def test_sorting_high_to_low(self, driver):
        sorting_kind = 'Price (high to low)'

        username = 'standard_user'
        form_page = FormPage(driver, "https://www.saucedemo.com/")
        form_page.open()
        form_page.login(username)

        main_page = MainPage(driver, "https://www.saucedemo.com/inventory.html")
        original_product_price = main_page.get_product_order_prices()

        main_page.select_sorting(sorting_kind)

        sorted_product_price = main_page.get_product_order_prices()

        expected_sorted_price = sorted(original_product_price, reverse=True)
        assert sorted_product_price == expected_sorted_price, f'Sorting {sorting_kind} failed'











