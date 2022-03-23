from .base_page import BasePage
from .locators import LoginPageLocators
from .main_page import MainPage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"text 'login' not found in url:{self.browser.current_url}"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_TEXTBOX).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_TEXTBOX1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_TEXTBOX2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
        self.should_be_authorized_user()
