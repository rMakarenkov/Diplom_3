import allure
from selenium.common import NoSuchFrameException

from data import LoginData
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем, что мы находимся на странице "Авторзация"')
    def login_title_is_present(self):
        return True if self.find_visability_element(*LoginPageLocators.LOGIN_TITLE) else False

    @allure.step('Заполняем поле "Email"')
    def set_email(self, ):
        self.find_clickable_element(*LoginPageLocators.INPUT_EMAIL).send_keys(LoginData.DEFAULT_USER.get('email'))

    @allure.step('Заполняем поле "Пароль"')
    def set_password(self):
        self.find_clickable_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(LoginData.DEFAULT_USER.get('password'))

    @allure.step('Нажимаем кнопку "Войти"')
    def press_button_login(self):
        self.find_clickable_element(*LoginPageLocators.BUTTON_LOGIN).click()

    @allure.step('Нажимаем на кнопку-ссылку "Восстановить пароль"')
    def click_button_link_restore_password(self):
        self.find_clickable_element(*LoginPageLocators.FORGOT_PASSWORD_LINK_BUTTON).click()

    @allure.step('Выполняем авторизацию пользователя')
    def authorization_user(self):
        if self.login_title_is_present():
            self.set_email()
            self.set_password()
            self.press_button_login()
        else:
            raise Exception('Failed to authorize user')
