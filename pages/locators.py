from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.XPATH, "//div[contains(@class, 'basket-mini')]/span/a[contains(@href, 'basket')]")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
     ADD_TO_BASKET_BTN = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
     PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/p[@class='price_color']")
     PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
     PRODUCT_DESCRIPTION_TITLE = (By.CSS_SELECTOR, "#product_description")
     PRODUCT_NAME_CONFIRMATION = (By.XPATH, "//div[@id='messages']/div[1]/div[1]/strong")
     PRODUCT_PRICE_CONFIRMATION = (By.XPATH, "//div[@id='messages']/div[3]//p[1]/strong")

class BasketPageLocators:
    BASKET_ITEMS_FORM = (By.CSS_SELECTOR, "#basket_formset")
    ELEMENT_WITH_NO_PRODUCTS_MSG = (By.XPATH, "//div[@id='content_inner']/p")
