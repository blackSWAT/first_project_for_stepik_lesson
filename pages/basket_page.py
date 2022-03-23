from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_basket(self):
        self.check_text_in_basket()
        self.check_empty_basket()

    def check_text_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), f"Element {BasketPageLocators.BASKET_EMPTY}" \
                                                                          f" not found"

    def check_empty_basket(self):
        assert self.is_disappeared(*BasketPageLocators.BASKET_WITH_PRODUCT), f"Element " \
                                                                        f"{BasketPageLocators.BASKET_WITH_PRODUCT}" \
                                                                        f" found"
