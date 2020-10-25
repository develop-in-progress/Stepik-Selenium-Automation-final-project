from selenium.webdriver.common.by import By
import pytest


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasketPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    EMPTY_TEXT = 'Your basket is empty. Continue shopping'


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_LINK_SELECTOR = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '[class="col-sm-6 login_form"]')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_FORM_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTRATION_FORM_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTRATION_FORM_CONFIRM = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    REGISTRATION_PASSWORD = '123asdqwe123'


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRODUCT_PAGE_LINK = \
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main > p')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main > h1')
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, '.alertinner > strong')
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alertinner > p > strong')

    PARAMETRIZE_LINKS = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                         pytest.param(
                             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                             marks=pytest.mark.xfail),
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]
