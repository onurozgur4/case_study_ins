import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

# Configure logging globally (you can adjust level/format as needed)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logging.info("BasePage initialized with WebDriver.")

    def open(self, url):
        logging.info(f"Opening URL: {url}")
        self.driver.get(url)

    def is_opened(self, title):
        logging.info(f"Verifying page title contains: '{title}'")
        assert title in self.driver.title, f"Expected title '{title}' not found in '{self.driver.title}'"
        logging.info("Page title verification passed.")

    def is_opened_with_url(self, url):
        current_url = self.driver.current_url
        logging.info(f"Verifying current URL contains: '{url}' (Actual URL: {current_url})")
        assert url in current_url, f"Expected URL '{url}' not found in '{current_url}'"
        logging.info("URL verification passed.")

    def click(self, locator):
        logging.info(f"Clicking element: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        logging.info("Element clicked successfully.")

    def get_element(self, locator):
        logging.info(f"Waiting for presence of element: {locator}")
        element = self.wait.until(EC.presence_of_element_located(locator))
        logging.info("Element found.")
        return element

    def get_elements(self, locator):
        logging.info(f"Waiting for presence of all elements: {locator}")
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        logging.info(f"Found {len(elements)} elements.")
        return elements
    
    def is_element_visible(self, locator):
        logging.info(f"Checking visibility of element: {locator}")
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            logging.info("Element is visible.")
            return True
        except:
            logging.warning("Element not visible.")
            return False
    
    def scroll_to(self, locator):
        logging.info(f"Scrolling to element: {locator}")
        element = self.wait.until(EC.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()
        logging.info("Scrolled to element successfully.")
        return element
