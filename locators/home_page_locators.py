from selenium.webdriver.common.by import By


class HomePageLocators:
    TITLE_ASSEMBLE_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")
    IMG_BUN_INGREDIENT = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    IMG_SAUCE_INGREDIENT = (By.XPATH, "//img[@alt='Соус Spicy-X']")
    BASKET = (By.CSS_SELECTOR, '.BurgerConstructor_basket__list__l9dp_')
    ELEMENTS_IN_BASKET = (By.XPATH, "//li[@class='BasketItem_basketItem__listItem__3yMU_ mb-4 mr-2']")
    BUTTON_PLACE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")

    LABEL_MODAL_WINDOW = (By.XPATH, "//h2[text()='Детали ингредиента']")
    BUTTON_CROSS_MODAL_DETAIL = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button")

    LABEL_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.undefined.text.text_type_main-small.mb-2')
    LOADING_MODAL_WINDOW_ORDER = (By.XPATH, "//div[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")
    ORDER_ID_MODAL_WINDOW = (By.CSS_SELECTOR, '.Modal_modal__title_shadow__3ikwq.Modal_modal__title__2L34m.text.text_type_digits-large.mb-8')
    BUTTON_CROSS_MODAL_ORDER = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
