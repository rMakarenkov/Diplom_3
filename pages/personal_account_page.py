import allure

from locators.personal_account_page_locators import PersonalAccountPageSelectors
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем наличие справочной информации и возвращаем текущий URL')
    def find_additional_info_and_return_current_url(self):
        self.find_visability_element(*PersonalAccountPageSelectors.LABEL_ADDITIONAL_INFO)
        return self.get_current_url()

    @allure.step('Нажимаем на раздел "История заказов"')
    def click_orders_history(self):
        self.find_clickable_element(*PersonalAccountPageSelectors.LABEL_ORDERS_HISTORY).click()

    @allure.step('Нажимаем на кнопку "Выход"')
    def click_logout(self):
        self.find_clickable_element(*PersonalAccountPageSelectors.BUTTON_LOGOUT).click()

    @allure.step('Получаем номер последнего заказа в списке заказов личного кабинета')
    def get_last_order_data(self):
        return self.find_visability_element(*PersonalAccountPageSelectors.LAST_ORDER_NUMBER_IN_ACC).text
