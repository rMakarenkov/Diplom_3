import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.timeout = timeout

    @allure.step('Открываем страницу: {url}')
    def open(self, url):
        self.driver.get(url)

    def find_clickable_element(self, how, what):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(ec.element_to_be_clickable((how, what)))
            return web_element

        except TimeoutException:
            raise TimeoutException(f'\nElement not clickable after {self.timeout} seconds')
        except Exception as e:
            raise Exception(f'\nAn error occurred while finding the clickable element: {e}')

    def find_visability_element(self, how, what):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located((how, what)))
            return web_element

        except TimeoutException:
            raise TimeoutException(f'\nElement not visability after {self.timeout} seconds')
        except Exception as e:
            raise Exception(f'\nAn error occurred while finding the visability element: {e}')

    def scroll_to_element(self, how, what):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located((how, what)))
            return self.driver.execute_script('arguments[0].scrollIntoView();', web_element)

        except TimeoutException:
            raise TimeoutException(f'\nElement not visability after {self.timeout} seconds')
        except Exception as e:
            raise Exception(f'\nAn unexpected error occurred while scrolling to the element: {e}')
