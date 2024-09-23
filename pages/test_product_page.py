from .base_page import BasePage
from .locators import ProducPageLocators

class ProductPage(BasePage):

    def should_be_product_page(self):
       self.is_product_description_title_present()

    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProducPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()
        self.solve_quiz_and_get_code()

    def is_product_description_title_present(self):
        assert self.is_element_present(*ProducPageLocators.PRODUCT_DESCRIPTION_TITLE), "There is no product description title"

    def get_product_name(self):
        return self.browser.find_element(*ProducPageLocators.PRODUCT_NAME).text

    def get_product_name_on_confirmation_page(self):
        return self.browser.find_element(*ProducPageLocators.PRODUCT_NAME_CONFIRMATION).text

    def get_product_price(self):
        return self.browser.find_element(*ProducPageLocators.PRODUCT_PRICE).text[1:]

    def get_product_price_on_confirmation_page(self):
        return self.browser.find_element(*ProducPageLocators.PRODUCT_PRICE_CONFIRMATION).text[1:]



