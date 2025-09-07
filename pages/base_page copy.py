import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def is_opened(self, title):
        assert  title in self.driver.title

    def is_opened_with_url(self, url):
        current_url = self.driver.current_url
        assert url in current_url

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def get_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            logging.info(f"Element is present: {locator}")
            return True
        except:
            logging.warning(f"Element not found: {locator}")
            return False
    
    def scroll_to(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()
