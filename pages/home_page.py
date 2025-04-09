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

    @allure.step('Нажимаем на ингредиент')
    def click_on_ingredient(self):
        self.find_clickable_element(*HomePageLocators.IMG_BUN_INGREDIENT).click()

    @allure.step('Ищем заголовок модального окна и возвращаем его текст')
    def find_title_modal_window_and_return_text(self):
        return self.find_visability_element(*HomePageLocators.LABEL_MODAL_WINDOW).text

    @allure.step('Закрываем модальное окно')
    def click_on_cross_in_modal_window(self):
        self.find_clickable_element(*HomePageLocators.BUTTON_CROSS).click()

    @allure.step('Проверяем, что модальное окно закрыто')
    def control_close_modal_window(self):
        return self.wait_element_disappears(*HomePageLocators.LABEL_MODAL_WINDOW)

    @allure.step('Перетаскиваем ингредиент в корзину')
    def drag_element_in_basket(self):
        self.drag_and_drop(*HomePageLocators.IMG_SAUCE_INGREDIENT, *HomePageLocators.BASKET)

    @allure.step('Получаем количество ингредиентов в корзине')
    def get_count_ingredients_in_basket(self):
        return self.get_count_elements(*HomePageLocators.ELEMENTS_IN_BASKET)

    @allure.step('Нажимаем на кнопку оформления заказа')
    def click_button_place_order(self):
        self.find_clickable_element(*HomePageLocators.BUTTON_PLACE_ORDER).click()

    @allure.step('Проверяем .................')
    def find_success_info_in_modal_window_order(self):
        return self.find_visability_element(*HomePageLocators.LABEL_SUCCESS_MESSAGE).text
