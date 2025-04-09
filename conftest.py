import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import urls
from pages.login_page import LoginPage


@allure.step('Открытие браузер')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = None
    if request.param == 'chrome':
        chrome_options = ChromeOptions()
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1920, 1080)
    elif request.param == 'firefox':
        firefox_options = FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)
        driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def login(driver):
    account = LoginPage(driver)
    account.open(urls.LOGIN_URL)
    account.authorization_user()
