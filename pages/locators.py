from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

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
