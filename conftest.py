import os
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option('detach', True)
    chrome_options.add_argument('--guest')
    chrome_options.add_argument('lang=en')

    #Headless in CI
    if os.getenv("CI"):
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        ChromeDriverManager().install(),
        options=chrome_options)
    
    driver.get("https://automationexercise.com")
    yield driver
    # driver.quit()

# Automatically attach screenshot, HTML source, and console logs on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only capture failures in the test execution phase (not setup/teardown)
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            # Screenshot
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"screenshot_{item.name}",
                attachment_type=allure.attachment_type.PNG
            )

            # HTML source
            allure.attach(
                driver.page_source,
                name=f"page_source_{item.name}",
                attachment_type=allure.attachment_type.HTML
            )

            # Browser console logs (Chrome only)
            try:
                logs = driver.get_log("browser")
                log_text = "\n".join([str(entry) for entry in logs])
                allure.attach(
                    log_text,
                    name=f"console_logs_{item.name}",
                    attachment_type=allure.attachment_type.TEXT
                )
            except Exception:
                # Some drivers or modes (headless) may not support logs
                pass
