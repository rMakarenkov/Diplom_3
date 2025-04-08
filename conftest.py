import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')


@pytest.fixture(scope='function')
def driver(request):
    driver = None
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        print('\n start browser chrome for test...')
        driver = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        print('\n Start browser firefox for test...')
        driver = webdriver.Firefox(options=options)
    else:
        print(f'Browser {browser_name} not currently implemented')
    yield driver
    print('\n Quit browser...')
    driver.quit()
