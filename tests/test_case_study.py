import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage
from pages.open_positions_page import OpenPositionsPage
from pages.jobs_lever_page import JobsLeverPage

def test_case_study(driver):
    home = HomePage(driver)
    careers = CareersPage(driver)
    qa_jobs = QAJobsPage(driver)
    open_positions = OpenPositionsPage(driver)
    jobs_lever = JobsLeverPage(driver)

    home.go_to_page()
    home.page_is_opened()
    home.accept_cookies()
    home.go_to_company_menu()
    home.go_to_careers_page()

    careers.page_is_opened()
    careers.location_section_is_visible()
    careers.teams_section_is_visible()
    careers.life_at_insider_section_is_visible()

    qa_jobs.go_to_page()
    qa_jobs.click_see_all_qa_jobs_button()

    open_positions.page_is_opened()
    open_positions.open_find_by_location_dropdown()
    open_positions.select_istanbul_on_dropdown()
    time.sleep(3) # Seach may take time!
    open_positions.scroll_to_first_job()
    open_positions.view_first_qa_job_in_istanbul()

    jobs_lever.page_is_opened()