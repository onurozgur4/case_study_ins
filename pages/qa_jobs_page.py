from selenium.webdriver.common.by import By
from .base_page import BasePage

class QAJobsPage(BasePage):
    QA_JOBS_PAGE_URL = "https://useinsider.com/careers/quality-assurance/"
    QA_JOBS_PAGE_TITLE = "Insider quality assurance job opportunities"
    SEE_ALL_QA_JOBS_BUTTON = (By.XPATH, "//*[@href='https://useinsider.com/careers/open-positions/?department=qualityassurance' and text()='See all QA jobs']")

    def go_to_page(self):
        self.open(self.QA_JOBS_PAGE_URL)

    def page_is_opened(self):
        self.is_opened(self.QA_JOBS_PAGE_TITLE)
    
    def click_see_all_qa_jobs_button(self):
        self.click(self.SEE_ALL_QA_JOBS_BUTTON)