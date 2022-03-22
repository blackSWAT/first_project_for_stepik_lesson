from .base_page import BasePage
from .locators import CartPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        link = self.browser.find_element(*CartPageLocators.BASKET)
        link.click()
        self.solve_quiz_and_get_code()

    def check_message_and_price(self):
        text = self.browser.find_element(*CartPageLocators.POPUP_ADD_CART).text
        book_name = self.browser.find_element(*CartPageLocators.BOOK_NAME).text
        assert text == book_name, f"Product Name {text} not equal {book_name}"
        sum_in_basket = self.browser.find_element(*CartPageLocators.SUM_IN_BASKET).text
        sum_in_product = self.browser.find_element(*CartPageLocators.SUM_IN_PRODUCT).text
        assert sum_in_product == sum_in_basket, f'''Price in basket:{sum_in_basket} not equal price product: 
                                                {sum_in_product}'''

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*CartPageLocators.POPUP_ADD_CART),\
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_element_present(*CartPageLocators.POPUP_ADD_CART),\
            "Success message not presented, but should be"

    def should_not_be_success_message_other(self):
        assert self.is_disappeared(*CartPageLocators.POPUP_ADD_CART), \
            "Success message is presented, but should not be"