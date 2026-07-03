from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    COOKIE_ACCEPT = (By.XPATH, "//div/button/p[contains (text(), Consent)]")  # real locator
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")

    def accept_cookies(self):
        try:
            self.click(self.COOKIE_ACCEPT)
        except:
            pass  # popup may not appear IN HEADLESS

    def go_to_login(self):
        self.click(self.LOGIN_LINK)
