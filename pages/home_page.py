import allure

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем переход на главную страницу')
    def find_home_page_title_and_return_current_url(self):
        self.find_visability_element(*HomePageLocators.TITLE_ASSEMBLE_BURGER)
        return self.get_current_url()
