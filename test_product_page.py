from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    page.open()
    page.click_add_button()
    page.solve_quiz_and_get_code()
    page.should_be_correct_name_in_basket_message()
    page.should_be_correct_price_in_basket_message()
    time.sleep(1)