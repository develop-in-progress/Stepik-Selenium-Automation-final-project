from .base_page import BasePage
from .locators import LoginPageLocators
import time
import allure


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    @allure.step('Login url is shown on the Login page')
    def should_be_login_url(self):
        assert self.browser.current_url == LoginPageLocators.LOGIN_LINK, 'Url is not the login page\'s url'

    @allure.step('Login form is shown on the Login page')
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'There is no login form on the Login page'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), \
            'There is no registration form on the Login page'

    def register_new_user(self):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_EMAIL)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASSWORD)
        password_field_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_CONFIRM)
        email = str(time.time()) + "@fakemail.org"
        email_field.send_keys(email)
        password_field.send_keys(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_field_confirm.send_keys(*LoginPageLocators.REGISTRATION_PASSWORD)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()
