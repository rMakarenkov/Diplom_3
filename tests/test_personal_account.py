import allure
import pytest

import urls
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage


@pytest.mark.perosnal_account_page
@allure.feature('Страница "Личный кабинет"')
class TestPersonalAccount:
    @allure.title('Проверка перехода в личный кабинет через кнопку в хедере')
    def test_go_to_personal_account_page_successful_transition(self, driver, auth_default_user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_button_link_personal_account()
        current_url = personal_account_page.find_additional_info_and_return_current_url()
        assert current_url == urls.PROFILE_URL, f'Actual url {current_url} not match expected url {urls.PROFILE_URL}'

    @allure.title('Проверка перехода в раздел "История заказов"')
    def test_go_to_orders_history_successful_transition(self, driver, auth_default_user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_button_link_personal_account()
        personal_account_page.click_orders_history()
        current_url = personal_account_page.find_additional_info_and_return_current_url()
        assert current_url == urls.PROFILE_ORDERS_HISTORY_URL, f'Actual url {current_url} not match expected url {urls.PROFILE_ORDERS_HISTORY_URL}'

    @allure.title('Проверка выхода из профиля')
    def test_logout_personal_account_successful_logout(self, driver, auth_default_user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_button_link_personal_account()
        personal_account_page.click_logout()
        login_page = LoginPage(driver)
        current_url = login_page.find_login_title_and_return_current_url()
        assert current_url == urls.LOGIN_URL, f'Actual url {current_url} not match expected url {urls.LOGIN_URL}'
