import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажимаем на кнопку-ссылку "Восстановить пароль"')
    def click_button_link_restore_password(self):
        self.find_clickable_element(*LoginPageLocators.FORGOT_PASSWORD_LINK_BUTTON).click()
