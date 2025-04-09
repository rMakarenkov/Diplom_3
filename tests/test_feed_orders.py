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
    def test_click_order_and_show_modal_window_successfull_showed(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open(urls.ORDER_FEED_URL)
        feed_page.click_order()
        assert feed_page.order_model_window_is_visible(), 'Modal window with order is not displayed'

    @allure.title('Заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_user_orders_show_in_order_feed_successfull_showed(self, driver, auth_default_user):
        home_page = HomePage(driver)
        home_page.drag_bun_in_basket()
        home_page.drag_sauce_in_basket()
        home_page.click_button_place_order()
        home_page.click_cross_in_order_modal_window()
        home_page.click_button_link_personal_account()
        account = PersonalAccountPage(driver)
        account.click_orders_history()
        last_order_number_in_account = account.get_last_order_data()
        account.click_button_link_order_feed()
        feed_page = FeedPage(driver)
        assert feed_page.find_target_order_in_history(
            last_order_number_in_account), 'The order you are looking for is not in the order feed'
