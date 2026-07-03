from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_login_valid_user(driver):
    home = HomePage(driver)
    home.accept_cookies()
    home.go_to_login()

    login = LoginPage(driver)
    login.login("kipeha4706@givmail.com", "Test123")

    assert login.is_logout_visible()

def test_login_invalid_user(driver):
    home = HomePage(driver)
    home.accept_cookies()
    home.go_to_login()

    login_page = LoginPage(driver)
    login_page.login("wrong@example.com", "wrongpasskkkk")

    assert driver.current_url.endswith("/login")
    assert not login_page.is_logout_visible()

