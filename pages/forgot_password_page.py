import allure

from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from data import ForgotPasswordData


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Вводим адрес электронной почты {email}')
    def enter_email(self, email=ForgotPasswordData.EMAIL):
        self.find_clickable_element(*ForgotPasswordPageLocators.INPUT_EMAIL).send_keys(email)

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def press_the_restore_button(self):
        self.find_clickable_element(*ForgotPasswordPageLocators.RESTORE_BUTTON).click()

    @allure.step('Нажимаем на кнопку "показать/скрыть" пароль')
    def press_the_show_hide_button(self):
        self.find_clickable_element(*ForgotPasswordPageLocators.EYE_BUTTON).click()

    @allure.step('Проверяем, что поле "Пароль" является активным (подсвечивается)')
    def input_password_is_illuminated(self):
        try:
            self.find_visability_element(*ForgotPasswordPageLocators.ACTIVE_INPUT_PASSWORD)
            return True
        except Exception as e:
            print(f'Error name: {type(e).__name__}, error message: {e}')
            return False
