from selenium.webdriver.common.by import By


class PersonalAccountPageSelectors:
    LABEL_ADDITIONAL_INFO = (By.CSS_SELECTOR, '.Account_text__fZAIn')
    LABEL_ORDERS_HISTORY = (By.XPATH, "//a[text()='История заказов']")
    LABEL_ORDERS_HISTORY_ACTIVE = (By.XPATH, "//a[text()='История заказов' and contains(@class,'Account_link_active__2opc9')]")
    LAST_ORDER_NUMBER_IN_ACC = (By.XPATH, "//div[@class='OrderHistory_orderHistory__qy1VB']"
                                          "//li[position()=last()]//p[@class='text text_type_digits-default']")
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")
