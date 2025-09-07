from selenium.webdriver.common.by import By
from .base_page import BasePage

class JobsLeverPage(BasePage):
    JOBS_LEVER_PAGE_TITLE = "Insider"

    def page_is_opened(self):
        self.is_opened(self.JOBS_LEVER_PAGE_TITLE)