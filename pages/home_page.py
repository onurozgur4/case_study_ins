from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    HOME_PAGE_URL = "https://useinsider.com/"
    HOME_PAGE_TITLE = "#1 Leader in Individualized, Cross-Channel CX — Insider"
    ACCEPT_COOKIES = (By.ID, "wt-cli-accept-all-btn")
    COMPANY_MENU = (By.XPATH, "//a[@id='navbarDropdownMenuLink' and contains(normalize-space(text()), 'Company')]")
    CAREERS_LINK = (By.XPATH, "//a[@href='https://useinsider.com/careers/']")

    def go_to_page(self):
        self.open(self.HOME_PAGE_URL)

    def page_is_opened(self):
        self.is_opened(self.HOME_PAGE_TITLE)

    def accept_cookies(self):
        self.click(self.ACCEPT_COOKIES)

    def go_to_company_menu(self):
        self.click(self.COMPANY_MENU)

    def go_to_careers_page(self):
        self.click(self.CAREERS_LINK)