import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
import pytest


@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.login_guest
class TestLoginFromMainPage:
    @allure.story('Guest can see login link')
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    @allure.story('Guest can see login form')
    def test_guest_should_see_login_form(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_form()
        page.should_be_login_url()


@allure.severity(allure.severity_level.CRITICAL)
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = BasketPage(browser, link)
    page.open()
    page.click_basket_button()
    page.basket_should_be_empty_text_is_presented()


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)
    page.open()
    page = BasketPage(browser, browser.current_url)
    page.click_basket_button()
    page.basket_should_be_empty_text_is_presented()
