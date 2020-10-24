from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_LINK_SELECTOR = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '[class="col-sm-6 login_form"]')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRODUCT_PAGE_LINK = \
        'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main > p')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main > h1')
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, '.alertinner > strong')
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alertinner > p > strong')