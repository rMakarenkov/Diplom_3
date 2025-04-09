from selenium.webdriver.common.by import By

from data import LoginData


class PersonalAccountPageSelectors:
    LABEL_ADDITIONAL_INFO = (By.CLASS_NAME, 'Account_text__fZAIn text text_type_main-default')
    LABEL_ORDERS_HISTORY = (By.XPATH, "//a[text()='История заказов']")
    LABEL_ORDERS_HISTORY_ACTIVE = (By.XPATH, "//a[text()='История заказов' and "
                                             "contains(@class,'Account_link_active__2opc9')]")

    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")
