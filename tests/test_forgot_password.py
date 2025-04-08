import allure
import urls

from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage


@allure.feature('Страница восстановления пароля')
class TestForgotPassword:
    @allure.title('Проверка переходов и работы элемента "показать / скрыть" пароль')
    @allure.description('В кейсе проверяются:'
                        '\n- Переход на страницу восстановления пароля по кнопке «Восстановить пароль»'
                        '\n- Ввод почты и клик по кнопке «Восстановить'
                        '\n- Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_hide_password_functionality_successfully_operations(self, driver):
        login_page = LoginPage(driver)
        login_page.open(urls.LOGIN_URL)
        login_page.click_button_link_restore_password()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.enter_email()
        forgot_password_page.press_the_restore_button()
        forgot_password_page.press_the_show_hide_button()
        assert forgot_password_page.input_password_is_illuminated(), ('The effect of the "Password" field being active '
                                                                      'is not displayed')
