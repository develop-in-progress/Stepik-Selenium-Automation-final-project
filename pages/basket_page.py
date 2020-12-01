from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    link = 'http://selenium1py.pythonanywhere.com/ru/basket/'

    def click_basket_button(self):
        button = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        button.click()

    def basket_should_be_empty_text_is_presented(self):
        message_text = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE)
        message_text = message_text.text
        assert message_text == BasketPageLocators.EMPTY_TEXT, \
            'Текст о том что корзина пуста не отображен : {}'.format(message_text)
