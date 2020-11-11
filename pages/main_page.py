from .base_page import BasePage
import allure


@allure.step('Creating page')
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


