from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    # Locators
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".login-form p")

    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href='/logout']")

    # Actions
    def login(self, email, password):
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    # def is_logout_visible(self):
    #     return self.is_visible(self.LOGOUT_LINK)

    def is_logout_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.LOGOUT_LINK))
            return True
        except:
            return False
