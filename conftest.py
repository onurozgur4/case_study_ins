import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import base64

@pytest.fixture(scope="session")
def driver():
    chromedriver_path = "./drivers/chromedriver"
    
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    prefs = {"profile.default_content_setting_values.cookies": 1}
    chrome_options.add_experimental_option("prefs", prefs)

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            reports_folder = "reports/"
            if not os.path.exists(reports_folder):
                os.makedirs(reports_folder)

            timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
            screenshot_path = f"{reports_folder}/{item.name}_{timestamp}.png"
            driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as f:
                img_base64 = base64.b64encode(f.read()).decode("utf-8")

            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(img_base64, mime_type="image/png"))
                rep.extra = extra