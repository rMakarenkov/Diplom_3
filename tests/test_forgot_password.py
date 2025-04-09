import allure
import pytest

import urls
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage


@pytest.mark.forgot_password_page
@allure.feature('Страница восстановления пароля')
class TestForgotPassword:
    @allure.title('Проверка перехода на страницу "Восстановление пароля" со страницы "Авторизация"')
    def test_go_to_password_recovery_page_successful_transition(self, driver):
        login_page = LoginPage(driver)
        login_page.open(urls.LOGIN_URL)
        login_page.click_button_link_restore_password()
        current_url = login_page.get_current_url()
        assert current_url == urls.FORGOT_PASSWORD_URL, f'Actual url {current_url} not match expected url {urls.FORGOT_PASSWORD_URL}'

    @allure.title('Проверка возможности ввода почты в поле "Email" и нажатия на кнопку "Восстановить"')
    def test_enter_email_and_click_restore_successful_operation(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open(urls.FORGOT_PASSWORD_URL)
        forgot_password_page.enter_email()
        forgot_password_page.press_the_restore_button()
        current_url = forgot_password_page.find_button_save_password_and_return_current_url()
        assert current_url == urls.RESET_PASSWORD_URL, f'Actual url {current_url} not match expected url {urls.RESET_PASSWORD_URL}'

    @allure.title('Проверка наличия эффекта фокуса у поля "Пароль" при нажатии на кнопку показать/скрыть')
    def test_click_show_hide_button_effect_displayed(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open(urls.FORGOT_PASSWORD_URL)
        forgot_password_page.enter_email()
        forgot_password_page.press_the_restore_button()
        forgot_password_page.press_the_show_hide_button()
        assert forgot_password_page.input_password_is_illuminated(), 'The effect of the "Password" field being active is not displayed'
