import os
import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import datetime
from selenoid_desires_caps import *


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store',
                     help="Choose single browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")
    parser.addoption("--selenium_grid", action="store", default=None,
                     help="runs all tests in Selenium Grid in parralel")
    parser.addoption("--selenoid", action="store", default=None,
                     help="runs all tests in Selenoid in parralel")


def pytest_generate_tests(metafunc):
    if "browser" in metafunc.fixturenames and metafunc.config.getoption("selenium_grid") is not None:
        metafunc.parametrize("browser", ['grid_firefox', 'grid_chrome'], indirect=True)
    elif "browser" in metafunc.fixturenames and metafunc.config.getoption("selenoid") is not None\
            and metafunc.config.getoption("selenoid") != "all":
        metafunc.parametrize("browser", ['selenoid_chrome', 'selenoid_firefox'], indirect=True)
    elif "browser" in metafunc.fixturenames and metafunc.config.getoption("selenoid") == "all":
        metafunc.parametrize("browser", ['selenoid_chrome', 'selenoid_firefox', 'selenoid_chrome_old',
                                         'selenoid_firefox_old'], indirect=True)
    elif "browser" in metafunc.fixturenames and metafunc.config.getoption("browser_name") == 'parallel':
        metafunc.parametrize("browser", ['chrome', 'firefox'], indirect=True)


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("intl.accept_languages", language)
    firefox_profile.update_preferences()
    # firefox_opts = webdriver.FirefoxOptions()
    # firefox_opts.add_argument('headless')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    options.add_argument("--no-sandbox")  # This make Chromium reachable
    options.add_argument("--no-default-browser-check")  # Overrides default choices
    options.add_argument("--no-first-run")
    options.add_argument("--disable-default-apps")
    options.add_argument('--no-sandbox')
    # options.add_argument("--headless")
    browser = None
    if browser_name == "chrome":
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser_name == "firefox":
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=firefox_profile)
    elif request.param == 'grid_firefox':
        browser = webdriver.Remote(  # Different url for access to Grid in docker for jenkins
            command_executor='http://localhost:4444/wd/hub',  # command_executor='http://seleniumhub:4444/wd/hub'
            desired_capabilities=webdriver.DesiredCapabilities.FIREFOX.copy(), browser_profile=firefox_profile)
    elif request.param == 'grid_chrome':
        browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=webdriver.DesiredCapabilities.CHROME.copy(), options=options)
    elif request.param == 'selenoid_chrome':
        browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=selenoid_chrome_caps, options=options)
    elif request.param == 'selenoid_firefox':
        browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=selenoid_ff_caps, browser_profile=firefox_profile)
    elif request.param == 'selenoid_chrome_old':  # This is second browser version in selenoid
        browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=selenoid_chrome_caps_old, options=options)
    elif request.param == 'selenoid_firefox_old':  # This is second browser version in selenoid
        browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=selenoid_ff_caps_old, browser_profile=firefox_profile)
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
