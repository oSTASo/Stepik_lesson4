from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    FORM_LOGIN = (By.CSS_SELECTOR, '#login_form')
    FORM_REGISTER = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators:
    BTN_ADD_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main p')
    BTN_BASKET = (By.CSS_SELECTOR, '.basket-mini a')
    CURRENT_NAME = (By.CSS_SELECTOR, '.alertinner strong')
    CURRENT_PRICE = (By.CSS_SELECTOR, '.table-striped tr:nth-child(4) td')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-child(1) .alertinner strong')


