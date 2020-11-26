import os
import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FFOptions
from webdriver_manager.utils import ChromeType
from allure_commons.types import AttachmentType


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#
#     # we only look at actual failing test calls, not setup/teardown
#     if rep.when == "call" and rep.failed:
#         try:
#             allure.attach(browser.get_screenshot_as_png(),
#                           name='Screenshot',
#                           attachment_type=allure.attachment_type.PNG)
#         except Exception as e:
#             print('Oh no, there is Exception attack ur code: ', e)


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")  # This make Chromium reachable
        options.add_argument("--no-default-browser-check")  # Overrides default choices
        options.add_argument("--no-first-run")
        options.add_argument("--disable-default-apps")
        # options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser_name == "firefox":
        # fp = webdriver.FirefoxProfile()
        # fp.set_preference("intl.accept_languages", language)
        # browser = webdriver.Firefox(firefox_profile=fp)
        options = FFOptions()
        options.headless = True
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        try:
            web_driver = item.funcargs['browser']
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#
#     # we only look at actual failing test calls, not setup/teardown
#     if rep.when == "call" and rep.failed:
#         pass
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     if report.when == 'call':
#         if report.failed:
#                 try:
#                     allure.attach(item.instance.browser.get_screenshot_as_png(),
#                                   name=item.name,
#                                   attachment_type=AttachmentType.PNG)
#                 except Exception as e:
#                     print('Allure error: ', e)

# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     rep = outcome.get_result()
#     marker = item.get_closest_marker("ui")
#     marker = True
#     if marker:
#         # if rep.when == "call" and rep.failed:  # we only look at actual failing test calls, not setup/teardown
#             try:
#                 allure.attach(item.instance.browser.get_screenshot_as_png(),
#                               name=item.name,
#                               attachment_type=allure.attachment_type.PNG)
#             except Exception as e:
#                 print(e)
