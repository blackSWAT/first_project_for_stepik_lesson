from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "div.login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "div.register_form")


class CartPageLocators:
    BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    POPUP_ADD_CART = (By.CSS_SELECTOR, "div.alertinner > strong")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    SUM_IN_BASKET = (By.CSS_SELECTOR, "div.alert-info strong")
    SUM_IN_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
