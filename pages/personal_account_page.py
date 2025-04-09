import allure

from locators.personal_account_page_locators import PersonalAccountPageSelectors
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем успешность перехода на страницу профиля')
    def find_user_email_and_return_current_url(self):
        self.find_visability_element(*PersonalAccountPageSelectors.LABEL_LOGIN_USER)
        return self.get_current_url()

    @allure.step('Нажимаем на раздел "История заказов"')
    def click_orders_history(self):
        self.find_clickable_element(*PersonalAccountPageSelectors.LABEL_ORDERS_HISTORY).click()

    @allure.step('Нажимаем на кнопку "Выход"')
    def click_logout(self):
        self.find_clickable_element(*PersonalAccountPageSelectors.BUTTON_LOGOUT).click()
