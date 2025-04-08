import allure

import urls
from data import LoginData
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем переход на страницу "Восстановление пароля"')
    def title_forgot_password_is_present(self):
        return True if self.find_visability_element(*ForgotPasswordPageLocators.TITLE_FORGOT_PASSWORD) else False

    @allure.step('Вводим адрес электронной почты {email}')
    def enter_email(self, email=LoginData.DEFAULT_USER.get('email')):
        self.find_clickable_element(*ForgotPasswordPageLocators.INPUT_EMAIL).send_keys(email)

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def press_the_restore_button(self):
        self.find_clickable_element(*ForgotPasswordPageLocators.BUTTON_RESTORE).click()

    @allure.step('Проверяем переход на страницу сброса пароля')
    def reset_password_page_is_present(self):
        return True if self.url_to_be(urls.RESET_PASSWORD_URL) else False

    @allure.step('Нажимаем на кнопку "показать/скрыть" пароль')
    def press_the_show_hide_button(self):
        self.find_clickable_element(*ForgotPasswordPageLocators.BUTTON_EYE).click()

    @allure.step('Проверяем, что поле "Пароль" является активным (подсвечивается)')
    def input_password_is_illuminated(self):
        return True if self.find_visability_element(*ForgotPasswordPageLocators.ACTIVE_INPUT_PASSWORD) else False
