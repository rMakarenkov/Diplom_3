from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    # forgot
    TITLE_FORGOT_PASSWORD = (By.XPATH, "//h2[text()='Восстановление пароля']")
    INPUT_EMAIL = (By.XPATH, "//input[@name='name']")
    BUTTON_RESTORE = (By.XPATH, "//button[text()='Восстановить']")
    # restore
    BUTTON_EYE = (By.CSS_SELECTOR, '.input__icon')
    ACTIVE_INPUT_PASSWORD = (By.CSS_SELECTOR, '.input_status_active')
