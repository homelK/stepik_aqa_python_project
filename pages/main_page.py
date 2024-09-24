from .base_page import BasePage
from .locators import BasePageLocators

class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)