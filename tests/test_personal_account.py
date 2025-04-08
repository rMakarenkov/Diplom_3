import time
import allure
import urls

from pages.login_page import LoginPage
from pages.home_page import HomePage


@allure.feature('Личный кабинет')
class TestPersonalAccount:
    @allure.title('Проверка доступности элементов личного кабинета и выход из аккаунта')
    @allure.description('В кейсе проверяются:'
                        '\n- Переход по клику на «Личный кабинет»'
                        '\n- Переход в раздел «История заказов»'
                        '\n- Выход из аккаунта')
    def test_orders_history_and_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.open(urls.LOGIN_URL)
        login_page.authorization_user()
        home_page = HomePage(driver)
        home_page.home_page_title_is_present()
        home_page.click_button_link_personal_account()
