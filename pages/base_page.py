import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.timeout = timeout

    @allure.step('Открываем страницу: {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    def wait_modal_disappears(self, how, what):
        try:
            return WebDriverWait(self.driver, self.timeout).until(ec.invisibility_of_element_located((how, what)))
        except TimeoutException:
            raise TimeoutException('Modal window did not hide')

    def url_to_be(self, url):
        try:
            return WebDriverWait(self.driver, self.timeout).until(ec.url_to_be(url))
        except TimeoutException:
            raise TimeoutException(f'URL did not become: {url}')

    def find_clickable_element(self, how, what):
        try:
            return WebDriverWait(self.driver, self.timeout).until(ec.element_to_be_clickable((how, what)))
        except TimeoutException:
            raise TimeoutException(f'\nElement not clickable after {self.timeout} seconds')

    def find_visability_element(self, how, what):
        try:
            return WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located((how, what)))
        except TimeoutException:
            raise TimeoutException(f'\nElement not visability after {self.timeout} seconds')

    def scroll_to_element(self, how, what):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located((how, what)))
            return self.driver.execute_script('arguments[0].scrollIntoView();', web_element)
        except TimeoutException:
            raise TimeoutException(f'\nElement not visability after {self.timeout} seconds')

    @allure.step('Нажимаем на кнопку "Конструктор" в заголовке страницы')
    def click_button_link_constructor(self):
        self.find_clickable_element(*BasePageLocators.BUTTON_CONSTRUCTOR).click()

    @allure.step('Нажимаем на кнопку "Лента заказов" в заголовке страницы')
    def click_button_link_order_feed(self):
        self.find_clickable_element(*BasePageLocators.BUTTON_ORDER_FEED).click()

    @allure.step('Нажимаем на кнопку "Личный кабинет в заголовке страницы')
    def click_button_link_personal_account(self):
        self.find_clickable_element(*BasePageLocators.BUTTON_PERSONAL_ACCOUNT).click()
