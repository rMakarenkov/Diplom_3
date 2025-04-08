from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    # forgot
    FORGOT_PASSWORD_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    INPUT_EMAIL = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    # restore
    EYE_BUTTON = (By.CSS_SELECTOR, '.input__icon')
    ACTIVE_INPUT_PASSWORD = (By.CSS_SELECTOR, '.input_status_active')
