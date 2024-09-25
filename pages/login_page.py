from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "It is not the login page, but should be"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present, but should be"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present, but should be"

    def type_email_to_register_form(self, email):
        email_field = self.find_element(*LoginPageLocators.EMAIL_FIELD_REGISTER_FORM)
        email_field.send_keys(email)

    def type_passw_to_register_form(self, passw):
        passw_field = self.find_element(*LoginPageLocators.PASSW_FIELD_REGISTER_FORM)
        passw_field.send_keys(passw)

    def confirm_passw_in_register_form(self, passw):
        passw_field = self.find_element(*LoginPageLocators.PASSW_CONFIRM_FIELD_REGISTER_FORM)
        passw_field.send_keys(passw)

    def submit_register_form(self):
        submit_btn = self.find_element(*LoginPageLocators.SUBMIT_BTN_REGISTER_FORM)
        submit_btn.click()
