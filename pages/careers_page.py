from selenium.webdriver.common.by import By
from .base_page import BasePage

class CareersPage(BasePage):
    CAREERS_PAGE_URL = "https://useinsider.com/careers/"
    CAREERS_PAGE_TITLE = "Insider Careers"
    LOCATIONS_SECTION = (By.ID, "career-our-location")
    TEAMS_SECTION = (By.ID, "career-find-our-calling")
    LIFE_AT_INSIDER_SECTION = (By.XPATH, "//*[contains(@class, 'elementor-heading-title') and text()='Life at Insider']")
    SEE_ALL_TEAMS_BUTTON = (By.XPATH, "//*[@id='career-find-our-calling']//*[text()='See all teams']")
    SEE_ALL_QA_JOBS_BUTTON = (By.XPATH, "//*[@href='https://useinsider.com/careers/quality-assurance/']//*[text()='Quality Assurance']")
    
    def go_to_page(self):
        self.open(self.CAREERS_PAGE_URL)

    def page_is_opened(self):
        self.is_opened(self.CAREERS_PAGE_TITLE)

    def location_section_is_visible(self):
        self.is_element_visible(self.LOCATIONS_SECTION)
    
    def teams_section_is_visible(self):
        self.is_element_visible(self.TEAMS_SECTION)
    
    def life_at_insider_section_is_visible(self):
        self.is_element_visible(self.LIFE_AT_INSIDER_SECTION)

    def click_see_all_teams_button(self):
        self.click(self.SEE_ALL_TEAMS_BUTTON)

    def click_see_all_qa_jobs_button(self):
        self.click(self.SEE_ALL_QA_JOBS_BUTTON)    
