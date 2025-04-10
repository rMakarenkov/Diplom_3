import allure
import pytest

import urls
from pages.feed_page import FeedPage
from pages.home_page import HomePage
from pages.personal_account_page import PersonalAccountPage


@pytest.mark.feed_page
@allure.feature('Страница "Лента заказов"')
class TestFeedOrders:
    @allure.title('Проверка отображения модального окна при нажатии на заказ')
    def test_click_order_and_show_modal_window_successful_showed(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open(urls.ORDER_FEED_URL)
        feed_page.click_order()
        assert feed_page.order_model_window_is_visible(), 'Modal window with order is not displayed'

    @allure.title('Заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_user_orders_show_in_order_feed_successful_showed(self, driver, auth_default_user):
        home_page = HomePage(driver)
        home_page.make_order()
        home_page.click_button_link_personal_account()
        account = PersonalAccountPage(driver)
        account.click_orders_history()
        last_order_number_in_account = account.get_last_order_data()
        account.click_button_link_order_feed()
        feed_page = FeedPage(driver)
        assert feed_page.find_target_order_in_history(
            last_order_number_in_account), 'The order you are looking for is not in the order feed'

    @allure.title('Проверка увеличения счетчика "Выполнено за всё время" при создании нового заказа')
    def test_total_counter_increases_after_new_order_successful_increases(self, driver, auth_default_user):
        feed_page = FeedPage(driver)
        feed_page.click_button_link_order_feed()
        total_old_value = feed_page.get_number_total_orders_in_history()
        feed_page.click_button_link_constructor()
        home_page = HomePage(driver)
        home_page.make_order()
        home_page.click_button_link_order_feed()
        total_new_value = feed_page.get_number_total_orders_in_history()
        assert total_new_value > total_old_value, 'The counter of orders completed for all time has not increased'

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" при создании нового заказа')
    def test_today_counter_increases_after_new_order_successful_increases(self, driver, auth_default_user):
        feed_page = FeedPage(driver)
        feed_page.click_button_link_order_feed()
        old_value = feed_page.get_number_orders_today()
        feed_page.click_button_link_constructor()
        home_page = HomePage(driver)
        home_page.make_order()
        home_page.click_button_link_order_feed()
        new_value = feed_page.get_number_orders_today()
        assert new_value > old_value, 'The counter of orders completed today has not increased'

    @allure.title('Проверка отображения номера заказа "В работе" на странице "Лента заказов"')
    def test_order_in_progress_displayed_on_feed_order_page(self, driver, auth_default_user):
        home_page = HomePage(driver)
        order_id = home_page.make_order()
        home_page.click_button_link_order_feed()
        feed_page = FeedPage(driver)
        assert feed_page.check_order_in_progress(order_id), 'The order is not in the "In progress" list'
