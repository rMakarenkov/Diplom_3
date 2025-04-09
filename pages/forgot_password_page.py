import allure

from data import LoginData
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем наличие кнопки "Восстановить" и возвращаем текущий URL')
    def find_button_restore_and_return_current_url(self):
        self.find_clickable_element(*ForgotPasswordPageLocators.BUTTON_RESTORE)
        return self.get_current_url()

    @allure.step('Вводим адрес электронной почты {email}')
    def enter_email(self, email=LoginData.DEFAULT_USER.get('email')):
        self.find_clickable_element(*ForgotPasswordPageLocators.INPUT_EMAIL).send_keys(email)

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def press_the_restore_button(self):
        self.find_clickable_element(*ForgotPasswordPageLocators.BUTTON_RESTORE).click()

    @allure.title('Проверяем наличие кнопки "Сохранить" и возвращаем текущий URL')
    def find_button_save_and_return_current_url(self):
        self.find_clickable_element(*ForgotPasswordPageLocators.BUTTON_SAVE)
        return self.get_current_url()

    @allure.step('Нажимаем на кнопку "показать/скрыть" пароль')
    def press_the_show_hide_button(self):
        self.find_clickable_element(*ForgotPasswordPageLocators.BUTTON_EYE).click()

    @allure.step('Проверяем, что поле "Пароль" является активным (подсвечивается)')
    def input_password_is_illuminated(self):
        return self.find_visability_element(*ForgotPasswordPageLocators.ACTIVE_INPUT_PASSWORD).is_displayed()
