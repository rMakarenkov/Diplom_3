from selenium.webdriver.common.by import By


class FeedPageLocators:
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    ICON_ORDER_NUMBER_ONE = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6' and position()=1]")
    ORDER_MODAL_WINDOW = (By.CSS_SELECTOR, '.Modal_modal_opened__3ISw4.Modal_modal__P3_V5')

    LAST_50_ORDERS_NUMBERS = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']//p[@class='text text_type_digits-default']")