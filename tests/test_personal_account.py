import allure
import pytest

import urls
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage


@pytest.mark.perosnal_account_page
@allure.feature('Личный кабинет')
class TestPersonalAccount:
    @allure.title('Проверка доступности элементов личного кабинета и выход из аккаунта')
    @allure.description('В кейсе проверяются:'
                        '\n- Переход по клику на «Личный кабинет»'
                        '\n- Переход в раздел «История заказов»'
                        '\n- Выход из аккаунта')
    def test_show_tabs_personal_account_and_logout_successfully_operations(self, driver):
        login_page = LoginPage(driver)
        login_page.open(urls.LOGIN_URL)
        login_page.authorization_user()
        home_page = HomePage(driver)
        home_page.click_button_link_personal_account()
        personal_account_page = PersonalAccountPage(driver)
        assert personal_account_page.personal_account_page_is_present(), 'Unsuccessful transition to profile page'
        personal_account_page.click_to_orders_history()
        assert personal_account_page.label_orders_history_is_illuminated(), ('Something went wrong when clicked '
                                                                             'on order history')
        personal_account_page.logout()
        assert login_page.login_title_is_present(), 'Incorrect redirect after logout'
