import allure

from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем, что находимся на главной странице')
    def home_page_title_is_present(self):
        return True if self.find_visability_element(*HomePageLocators.TITLE_ASSEMBLE_BURGER) else False
