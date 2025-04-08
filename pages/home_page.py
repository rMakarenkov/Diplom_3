import allure

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем переход на главную страницу')
    def home_page_title_is_present(self):
        return True if self.find_visability_element(*HomePageLocators.TITLE_ASSEMBLE_BURGER) else False
