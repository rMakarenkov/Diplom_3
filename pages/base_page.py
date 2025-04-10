import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
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

    def wait_element_disappears(self, how, what):
        try:
            return WebDriverWait(self.driver, self.timeout).until(ec.invisibility_of_element_located((how, what)))
        except TimeoutException:
            raise TimeoutException(f'Modal window did not hide after {self.timeout} seconds')

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

    def text_present_in_element(self, how, what, text):
        try:
            return WebDriverWait(self.driver, self.timeout).until(ec.text_to_be_present_in_element((how, what), text))
        except TimeoutException:
            raise TimeoutException(f'\nElement not present in element after {self.timeout} seconds')

    def find_visability_element(self, how, what):
        try:
            return WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located((how, what)))
        except TimeoutException:
            raise TimeoutException(f'\nElement not visability after {self.timeout} seconds')

    def presence_of_elements(self, how, what):
        try:
            return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_all_elements_located((how, what)))
        except TimeoutException:
            raise TimeoutException(f'\nElements not present after {self.timeout} seconds')

    def scroll_to_element(self, how, what):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located((how, what)))
            return self.driver.execute_script('arguments[0].scrollIntoView();', web_element)
        except TimeoutException:
            raise TimeoutException(f'\nElement not visability after {self.timeout} seconds')

    def drag_and_drop(self, how_s, what_s, how_t, what_t):
        source = self.find_clickable_element(how_s, what_s)
        target = self.find_visability_element(how_t, what_t)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    def get_count_elements(self, how, what):
        count = len(self.driver.find_elements(how, what))
        return count

    @allure.step('Нажимаем на кнопку "Конструктор" в заголовке страницы')
    def click_button_link_constructor(self):
        self.find_clickable_element(*BasePageLocators.BUTTON_CONSTRUCTOR).click()

    @allure.step('Нажимаем на кнопку "Лента заказов" в заголовке страницы')
    def click_button_link_order_feed(self):
        self.find_clickable_element(*BasePageLocators.BUTTON_ORDER_FEED).click()

    @allure.step('Нажимаем на кнопку "Личный кабинет в заголовке страницы')
    def click_button_link_personal_account(self):
        self.find_clickable_element(*BasePageLocators.BUTTON_PERSONAL_ACCOUNT).click()
