import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')


@pytest.fixture(scope='function')
def driver(request):
    driver = None
    browser_name = request.config.getoption('browser_name')
    options = Options()
    options.add_argument("--start-maximized")
    if browser_name == 'chrome':
        print('\n start browser chrome for test...')
        driver = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('\n Start browser firefox for test...')
        driver = webdriver.Firefox(options=options)
    else:
        print(f'Browser {browser_name} not currently implemented')
    yield driver
    print('\n Quit browser...')
    driver.quit()
