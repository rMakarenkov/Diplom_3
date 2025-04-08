from selenium.webdriver.common.by import By


class PersonalAccountPageSelectors:
    LABEL_PROFILE = (By.XPATH, "//a[text()='Профиль']")
    LABEL_PROFILE_ACTIVE = (By.XPATH, "//a[text()='Профиль' and contains(@class,'Account_link_active__2opc9')]")
    LABEL_ORDERS_HISTORY = (By.XPATH, "//a[text()='История заказов']")
    LABEL_ORDERS_HISTORY_ACTIVE = (By.XPATH, "//a[text()='История заказов' and "
                                             "contains(@class,'Account_link_active__2opc9')]")

    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")
