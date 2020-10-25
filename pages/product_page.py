from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_button(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def should_be_correct_price_in_basket_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_product_price = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE).text
        assert product_price == basket_product_price, 'Product\'s name in basket is different'

    def should_be_correct_name_in_basket_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_product_name = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text
        assert product_name == basket_product_name, 'Product\'s price in basket is different'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)


