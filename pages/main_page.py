from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def click_show_basket(self):
        self.browser.find_element(*MainPageLocators.SHOW_BASKET).click()

    def check_message_empty_basket(self):
        current_language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        language = {'en': 'Your basket is empty.', 'ru': 'Ваша корзина пуста'}
        if language[current_language] in self.browser.find_element(*MainPageLocators.BASKET_EMPTY).text:
            return True
        else:
            return False



