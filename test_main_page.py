from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
import pytest

raise Exception('Should fail check1')
@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, link)
        self.page.open()
        self.page.should_be_login_link()

    def test_guest_should_see_login_form(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.should_be_login_form()
        self.page.should_be_login_url()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = BasketPage(browser, link)
    page.open()
    page.click_basket_button()
    page.basket_should_be_empty_text_is_presented()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)
    page.open()
    page = BasketPage(browser, browser.current_url)
    page.click_basket_button()
    page.basket_should_be_empty_text_is_presented()

