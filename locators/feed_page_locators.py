from selenium.webdriver.common.by import By


class FeedPageLocators:
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    ICON_ORDER_NUMBER_ONE = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6' and position()=1]")
    ORDER_MODAL_WINDOW = (By.CSS_SELECTOR, '.Modal_modal_opened__3ISw4.Modal_modal__P3_V5')
    LAST_50_ORDERS = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']"
                                "//p[@class='text text_type_digits-default']")
    TOTAL_ORDERS = (By.XPATH, "//div[@class='undefined mb-15']"
                              "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    TODAY_ORDERS = (By.XPATH, "//div[@class='OrderFeed_ordersData__1L6Iv']"
                              "//div[3]//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']"
                                    "//li[@class='text text_type_digits-default mb-2']")