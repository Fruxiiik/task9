from selenium.webdriver.common.by import By


class MainPageLocator:

    MENU_BUTTON = (By.CSS_SELECTOR, '#react-burger-menu-btn')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '#logout_sidebar_link')
    ADD_TO_CART_BUTTON = lambda button_name: (By.NAME, f"add-to-cart-{button_name}")
    REMOVE_FROM_CART_BUTTON = lambda button_name: (By.NAME, f"remove-{button_name}")
    CART_LINK = (By.CSS_SELECTOR, '#shopping_cart_container')
    CART_COUNTER = (By.CLASS_NAME, 'shopping_cart_badge')
    SORT_DROPDOWN = (By.CLASS_NAME, 'product_sort_container')
    SORT_OPTION = lambda sorting_kind: (By.XPATH, f"//option[text()='{sorting_kind}']")
    PRODUCT_ELEMENTS = (By.CLASS_NAME, 'inventory_item_name')
    PRODUCT_PRICES = (By.CLASS_NAME, 'inventory_item_price')

