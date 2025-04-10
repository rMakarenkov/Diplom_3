import allure

from data import LoginData
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем переход на страницу "Авторзация"')
    def find_login_title_and_return_current_url(self):
        self.find_visability_element(*LoginPageLocators.LOGIN_TITLE)
        return self.get_current_url()

    @allure.step('Заполняем поле "Email"')
    def set_email(self, ):
        self.find_clickable_element(*LoginPageLocators.INPUT_EMAIL).send_keys(LoginData.DEFAULT_USER.get('email'))

    @allure.step('Заполняем поле "Пароль"')
    def set_password(self):
        self.find_clickable_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(LoginData.DEFAULT_USER.get('password'))

    @allure.step('Нажимаем кнопку "Войти"')
    def click_button_login(self):
        self.find_clickable_element(*LoginPageLocators.BUTTON_LOGIN).click()

    @allure.step('Нажимаем на кнопку-ссылку "Восстановить пароль"')
    def click_restore_password(self):
        self.find_clickable_element(*LoginPageLocators.FORGOT_PASSWORD_LINK_BUTTON).click()

    @allure.step('Выполняем авторизацию пользователя')
    def authorization_user(self):
        self.set_email()
        self.set_password()
        self.click_button_login()
