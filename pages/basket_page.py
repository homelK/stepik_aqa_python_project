from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_FORM), "Basket is not empty, but should be"

    def should_be_element_with_no_products_msg(self):
        assert self.is_element_present(*BasketPageLocators.ELEMENT_WITH_NO_PRODUCTS_MSG), "No element with message about the empty basket, but should be"