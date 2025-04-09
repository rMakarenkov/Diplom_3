from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    # forgot
    INPUT_EMAIL = (By.XPATH, "//input[@name='name']")
    BUTTON_RESTORE = (By.XPATH, "//button[text()='Восстановить']")
    BUTTON_SAVE = (By.XPATH, "//button[text()='Сохранить']")
    # restore
    BUTTON_EYE = (By.CSS_SELECTOR, '.input__icon')
    ACTIVE_INPUT_PASSWORD = (By.CSS_SELECTOR, '.input_status_active')
