import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FFOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")



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
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)
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
