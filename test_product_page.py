from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.locators import LoginPageLocators
import pytest
from .pages.login_page import LoginPage


@pytest.mark.parametrize('link', ProductPageLocators.PARAMETRIZE_LINKS[0])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, ProductPageLocators.PARAMETRIZE_LINKS)
    page.open()
    page.click_add_button()
    page.solve_quiz_and_get_code()
    page.should_be_correct_name_in_basket_message()
    page.should_be_correct_price_in_basket_message()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    page.should_be_login_page()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.user_page = LoginPage(browser, LoginPageLocators.LOGIN_LINK)
        self.user_page.open()
        self.user_page.register_new_user()
        self.user_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
        page.open()
        page.click_add_button()
        page.should_be_correct_name_in_basket_message()
        page.should_be_correct_price_in_basket_message()
