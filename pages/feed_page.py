import allure

from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем переход на главную страницу и возвращаем текущий URL')
    def find_feed_page_title_and_return_current_url(self):
        self.find_visability_element(*FeedPageLocators.FEED_TITLE)
        return self.get_current_url()
