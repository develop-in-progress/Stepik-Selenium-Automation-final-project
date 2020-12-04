import os
import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import datetime
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def pytest_addoption(parser): # default='chrome',
    parser.addoption('--browser_name', action='store',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")
    parser.addoption("--grid", action="store", help="runs all tests in Selenium Grid in parralel")


def pytest_generate_tests(metafunc):
    try:
        if "browser" in metafunc.fixturenames and metafunc.config.getoption("browser_name") == 'grid':
            metafunc.parametrize("browser", ['grid_firefox', 'grid_chrome'], indirect=True)
    except ValueError as e:
        pass
    try:
        if "browser" in metafunc.fixturenames \
                and metafunc.config.getoption("browser_name") == 'parallel':
            metafunc.parametrize("browser", ['parallel_chrome', 'parallel_firefox'], indirect=True)
    except ValueError as e:
        pass


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    firefox_opts = webdriver.FirefoxProfile()
    firefox_opts.set_preference("intl.accept_languages", language)
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    options.add_argument("--no-sandbox")  # This make Chromium reachable
    options.add_argument("--no-default-browser-check")  # Overrides default choices
    options.add_argument("--no-first-run")
    options.add_argument("--disable-default-apps")
    options.add_argument('--no-sandbox')
    # options.add_argument("--headless")
    try:
        if browser_name == "chrome" or request.param == 'parallel_chrome':
            browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    except AttributeError:
        print("Invalid browser_name: {}".format(browser_name))
    try:
        if browser_name == "firefox" or request.param == 'parallel_firefox':
            browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=firefox_opts)
    except AttributeError:
        print("Invalid browser_name: {}".format(browser_name))
    try:
        if browser_name == 'grid_firefox' or request.param == 'grid_firefox':
            browser = webdriver.Remote(   # Different url for access to Grid in docker for jenkins
                command_executor='http://localhost:4444/wd/hub',   # command_executor='http://seleniumhub:4444/wd/hub'
                desired_capabilities=DesiredCapabilities.FIREFOX, browser_profile=firefox_opts)
    except AttributeError:
        print("Invalid browser_name: {}".format(browser_name))
    try:
        if browser_name == 'grid_chrome' or request.param == 'grid_chrome':
            browser = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME, options=options)
    except AttributeError:
        print("Invalid browser_name: {}".format(browser_name))

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
