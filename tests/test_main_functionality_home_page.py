import allure
import pytest

import urls
from pages.feed_page import FeedPage
from pages.home_page import HomePage


@pytest.mark.home_page
@allure.feature('Страница "Летна заказов"')
class TestMainFunctionalityHomePage:
    @allure.title('Проверка перехода на главную страницу ("Конструктор")')
    def test_go_to_constructor_successful_transition(self, driver):
        home_page = HomePage(driver)
        home_page.open(urls.LOGIN_URL)
        home_page.click_button_link_constructor()
        current_url = home_page.find_home_page_title_and_return_current_url()
        assert current_url == urls.BASE_URL, f'Actual url {current_url} not match expected url {urls.BASE_URL}'

    @allure.title('Проверка перехода на страницу "Лента заказов"')
    def test_go_to_feed_page_successful_transition(self, driver):
        home_page = HomePage(driver)
        home_page.open(urls.BASE_URL)
        home_page.click_button_link_order_feed()
        feed_page = FeedPage(driver)
        current_url = feed_page.find_feed_page_title_and_return_current_url()
        assert current_url == urls.ORDER_FEED_URL, f'Actual url {current_url} not match expected url {urls.ORDER_FEED_URL}'

    @allure.title('Проверяем отображение всплывающего окна с деталями при клике на ингредиент')
    def test_click_on_ingredient_and_show_details_successful_showed(self, driver):
        home_page = HomePage(driver)
        home_page.open(urls.BASE_URL)
        home_page.click_on_ingredient()
        expected_text = 'Детали ингредиента'
        actual_text = home_page.find_title_modal_window_and_return_text()
        assert actual_text == expected_text, f'Actual text {actual_text} not match expected text {expected_text}'

    @allure.title('Проверяем закрытие модального окна с доп. инфомрацией об ингредиенте при нажатии на крестик')
    def test_close_modal_window_after_click_cross_successfull_closed(self, driver):
        home_page = HomePage(driver)
        home_page.open(urls.BASE_URL)
        home_page.click_on_ingredient()
        home_page.click_on_cross_in_modal_window()
        assert home_page.control_close_modal_window(), 'Modal window not closed'

    @allure.title('Проверяем добавление ингредиента в заказ и увеличение каунтер данного ингредиента')
    def test_add_ingredient_and_check_count_counter_increases(self, driver):
        home_page = HomePage(driver)
        home_page.open(urls.BASE_URL)
        home_page.drag_element_in_basket()
        first_addition = home_page.get_count_ingredients_in_basket()
        home_page.drag_element_in_basket()
        second_addition = home_page.get_count_ingredients_in_basket()
        assert second_addition > first_addition, 'The counter of items in the basket does not increase'

    @allure.title('Проверяем оформление заказа авторизованным пользователем')
    def test_create_order_user_authorized_successfull_created(self, driver, auth_default_user):
        home_page = HomePage(driver)
        home_page.drag_element_in_basket()
        home_page.click_button_place_order()
        actual_message = home_page.find_success_info_in_modal_window_order()
        expected_message = 'Ваш заказ начали готовить'
        assert actual_message == expected_message, f'Actual message {actual_message} not match expected message {expected_message}'
