from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "div.login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "div.register_form")
    EMAIL_TEXTBOX = (By.CSS_SELECTOR, "input#id_registration-email")
    PASSWORD_TEXTBOX1 = (By.CSS_SELECTOR, "input#id_registration-password1")
    PASSWORD_TEXTBOX2 = (By.CSS_SELECTOR, "input#id_registration-password2")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")

class CartPageLocators:
    BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    POPUP_ADD_CART = (By.CSS_SELECTOR, "div.alertinner > strong")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    SUM_IN_BASKET = (By.CSS_SELECTOR, "div.alert-info strong")
    SUM_IN_PRODUCT = (By.CSS_SELECTOR, "p.price_color")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE = (By.CSS_SELECTOR, "span.btn-group > a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_WITH_PRODUCT = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_EMPTY = (By.CSS_SELECTOR, "div#content_inner > p > a")
