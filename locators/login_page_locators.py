from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")
    INPUT_EMAIL = (By.XPATH, "//input[@type='text']")
    INPUT_PASSWORD = (By.XPATH, "//input[@type='password']")
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")
    FORGOT_PASSWORD_LINK_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")
