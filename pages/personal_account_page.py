import allure

from data import LoginData
from locators.personal_account_page_locators import PersonalAccountPageSelectors
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем переход на страницу профиля')
    def personal_account_page_is_present(self):
        email = self.find_visability_element(*PersonalAccountPageSelectors.LABEL_LOGIN_USER).get_attribute('value')
        return True if email == LoginData.DEFAULT_USER.get('email') else False

    @allure.step('Нажимаем на раздел "История заказов"')
    def click_to_orders_history(self):
        self.find_clickable_element(*PersonalAccountPageSelectors.LABEL_ORDERS_HISTORY).click()

    @allure.step('Проверяем, что лейбл "История заказов" является активным (подсвечивается)')
    def label_orders_history_is_illuminated(self):
        return True if self.find_visability_element(
            *PersonalAccountPageSelectors.LABEL_ORDERS_HISTORY_ACTIVE) else False

    @allure.step('Нажимаем на кнопку "Выход"')
    def logout(self):
        self.find_clickable_element(*PersonalAccountPageSelectors.BUTTON_LOGOUT).click()
