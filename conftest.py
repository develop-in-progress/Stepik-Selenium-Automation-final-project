import os
import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FFOptions
import datetime
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")
    parser.addoption("--grid", action="store", default=None)


#
# def get_grid_driver_chrome():
#     browser = webdriver.Remote(
#                 command_executor='http://localhost:4444/wd/hub',
#                 desired_capabilities=DesiredCapabilities.CHROME)
#     yield browser
#     browser.quit()
#
#
# def get_grid_driver_firefox():
#     browser = webdriver.Remote(
#         command_executor='http://localhost:4444/wd/hub',
#         desired_capabilities=DesiredCapabilities.FIREFOX)
#     yield browser
#     browser.quit()
#
# f = get_grid_driver_firefox()
#
#
# def pytest_generate_tests(metafunc):
#     # This is called for every test. Only get/set command line arguments
#     # if the argument is specified in the list of test "fixturenames".
#     option_value = metafunc.config.option.grid
#     if 'browser' in metafunc.fixturenames and option_value is not None:
#         metafunc.parametrize("browser", [
#             get_grid_driver_chrome(),
#             f]
#                              )


# def caps():
#     return [DesiredCapabilities.CHROME, DesiredCapabilities.FIREFOX]


#
# def return_browser_name(request):
#     print('---'*33)
#     print(request.config.getoption("browser_name"))
#     browser = request.config.getoption("browser_name")
#     return browser


# @pytest.fixture(params=caps() if 'grid' in  else ['only_one_browser_will_init'])
# @pytest.fixture(params=caps())
# def get_caps(request):
#     return request.param


params = [('Chrome_for_grid', DesiredCapabilities.CHROME),
          ('Firefox_for_grid', DesiredCapabilities.FIREFOX)]


@pytest.fixture()
def return_browser_name(request):
    browser = request.config.getoption("browser_name")
    return browser


s = return_browser_name


@pytest.fixture(scope="function", params=params)
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        options.add_argument("--no-sandbox")  # This make Chromium reachable
        options.add_argument("--no-default-browser-check")  # Overrides default choices
        options.add_argument("--no-first-run")
        options.add_argument("--disable-default-apps")
        # options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser_name == "firefox":
        options = FFOptions()
        # options.headless = True
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    elif browser_name == 'grid':
        browser = webdriver.Remote(
            command_executor='http://seleniumhub:4444/wd/hub',
            desired_capabilities=request.param[1])
        # browser = webdriver.Remote(
        #     command_executor='http://localhost:4444/wd/hub',
        #     desired_capabilities=get_caps)
    elif browser_name == 'grid_firefox':
        browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)
    elif browser_name == 'grid_chrome':
        browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
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
        try:  # Just to not crash py.test reporting
            log = os.path.dirname(os.path.abspath(__file__))
            with open(str(os.path.join(log, 'logging.txt')), "a") as f:
                f.write(str(datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")) + "\n" + rep.longreprtext)
        except Exception as e:
            print("Logging err: ", e)
            pass
