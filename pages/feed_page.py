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

    @allure.step('Нажимаем на первый заказ в списке')
    def click_order(self):
        self.find_clickable_element(*FeedPageLocators.ICON_ORDER_NUMBER_ONE).click()

    @allure.step('Выполняем проверку отображения модального окна с деталями заказа')
    def order_model_window_is_visible(self):
        return self.find_visability_element(*FeedPageLocators.ORDER_MODAL_WINDOW).is_displayed()

    @allure.step('Просматриваем последние заказы и проверяем наличие искомого')
    def find_target_order_in_history(self, target_order):
        orders = self.presence_of_elements(*FeedPageLocators.LAST_50_ORDERS)
        return any(target_order == order.text for order in orders)

    @allure.step('Получаем количество выполненных заказов за все время')
    def get_number_total_orders_in_history(self):
        return self.find_visability_element(*FeedPageLocators.TOTAL_ORDERS).text

    @allure.step('Получаем количество выполненныз заказов за сегодняшний день')
    def get_number_orders_today(self):
        return self.find_visability_element(*FeedPageLocators.TODAY_ORDERS).text

    @allure.step('Проверяем наличие заказа в списке "В работе"')
    def check_order_in_progress(self, order_id):
        return self.text_present_in_element(*FeedPageLocators.ORDERS_IN_PROGRESS, order_id)
