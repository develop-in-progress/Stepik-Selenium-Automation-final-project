from .base_page import BasePage
from .locators import BasketPageLocators
import allure


@allure.step('Creating basket page')
class BasketPage(BasePage):
    link = 'http://selenium1py.pythonanywhere.com/ru/basket/'

    @allure.step('Clicking the basket button')
    def click_basket_button(self):
        button = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        button.click()

    @allure.step('Text on empty basket is shown')
    def basket_should_be_empty_text_is_presented(self):
        message_text = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE)
        message_text = message_text.text
        assert message_text == BasketPageLocators.EMPTY_TEXT, \
            'Текст о том что корзина пуста не отображен'



