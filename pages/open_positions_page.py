from selenium.webdriver.common.by import By
from .base_page import BasePage

class OpenPositionsPage(BasePage):
    OPEN_POSITIONS_PAGE_URL = "https://useinsider.com/careers/open-positions/"
    OPEN_POSITIONS_PAGE_TITLE = "Insider Open Positions | Insider"
    FIND_BY_LOCATION_DROPDOWN = (By.ID, "select2-filter-by-location-container")
    FIND_BY_DEPARTMAND_IS_SELECTED_QA = (By.XPATH, "//*[@id='select2-filter-by-department-container' and @title='Quality Assurance']")
    ISTANBUL_ON_LOCATION_DROPDOWN = (By.XPATH, "//li[contains(@class,'select2-results__option') and text()='Istanbul, Turkiye']")
    VIEW_FIRST_JOB = (By.XPATH, "(//*[contains(@class,'position-list-item-wrapper')])[1]")
    VIEW_FIRST_QA_JOB_IN_ISTANBUL_BUTTON = (By.XPATH, "(//*[contains(@class,'position-list-item-wrapper')][.//*[contains(text(),'Quality Assurance')]])[1]//a")

    def go_to_page(self):
        self.open(self.OPEN_POSITIONS_PAGE_URL)

    def page_is_opened(self):
        self.is_opened(self.OPEN_POSITIONS_PAGE_TITLE)

    def open_find_by_location_dropdown(self):
        self.is_element_visible(self.FIND_BY_DEPARTMAND_IS_SELECTED_QA)
        self.click(self.FIND_BY_LOCATION_DROPDOWN)
    
    def select_istanbul_on_dropdown(self):
        self.click(self.ISTANBUL_ON_LOCATION_DROPDOWN)

    def scroll_to_first_job(self):
        self.scroll_to(self.VIEW_FIRST_JOB)        

    def view_first_qa_job_in_istanbul(self):
        self.click(self.VIEW_FIRST_QA_JOB_IN_ISTANBUL_BUTTON)
