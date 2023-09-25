from pages.form_page import FormPage
from pages.main_page import MainPage


class TestFormPage:

    def test_login(self, driver):
        username = 'standard_user'
        form_page = FormPage(driver, "https://www.saucedemo.com/")
        form_page.open()
        form_page.login(username)
        assert "inventory.html" in driver.current_url, 'Login failed'

    def test_logout(self, driver):
        self.test_login(driver)

        main_page = MainPage(driver, "https://www.saucedemo.com/inventory.html")
        main_page.open()
        main_page.logout()
        assert "https://www.saucedemo.com/" in driver.current_url, 'Logout failed'

    def test_locked_out_login(self, driver):
        locked_out_username = 'locked_out_user'
        form_page = FormPage(driver, "https://www.saucedemo.com/")
        form_page.open()
        form_page.login(locked_out_username)
        error_message = form_page.find_error()
        assert "Epic sadface: Sorry, this user has been locked out." in error_message.text, \
            'Error due to blocked user not found'






