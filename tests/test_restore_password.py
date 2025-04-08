import allure
import urls

from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage


@allure.feature('Восстановление пароля')
class TestRestorePassword:
    @allure.title('Кейс проверки переходов на страницу "Восстановление пароля"')
    @allure.description('В кейсе проверяются:'
                        '\n- Переход на страницу восстановления пароля по кнопке «Восстановить пароль»'
                        '\n- Ввод почты и клик по кнопке «Восстановить'
                        '\n- Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_password_recovery_and_show_hide_password_functionality_successfully_operations(self, driver):
        # Arrange
        login_page = LoginPage(driver)
        login_page.open(urls.LOGIN_URL)
        login_page.click_button_link_restore_password()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.enter_email()
        forgot_password_page.press_the_restore_button()
        # Act
        forgot_password_page.press_the_show_hide_button()
        # Assert
        assert forgot_password_page.input_password_is_illuminated(), ('The effect of the "Password" field being active '
                                                                      'is not displayed')
