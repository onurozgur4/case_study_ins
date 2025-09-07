# case_study_ins

Automates testing of Company's Careers pages using **Python, Selenium, and pytest** with **Page Object Model (POM)**.

## Features
- Object-oriented page classes (`Home`, `Careers`, `QAJobs`, `OpenPositions`, `JobsLever`)
- ChromeOptions configured to **disable notifications** and **auto-accept cookies**
- Logging integrated for pytest-html reporting for **report file** and capturing **screen-shot** for test failures


## Project Structure
- **drivers/** - Folder for adding driver of browsers
- **pages/** - Page objects and locators
- **reports/** - Report.html file and ScreenShots (.png)
- **tests/** - Test cases
- **conftest.py** - Pytest fixtures for ChromeDriver
- **pytest.ini** - Test Execution configuration (PyTest)
- **requirements.txt** - Python dependencies

## Installation
**Python Requirement**
- Ensure **Python 3.10 or higher** is installed on your system.
- Verify installation and version:
    ```bash
    python3 --version
    ```

1. **Clone the repository**
    ```bash
    git clone <repository_url>
    cd case_study_onur/
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install depencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Install Chrome Driver**

    4.1 Download the correct version of ChromeDriver that matches your installed Google Chrome version: https://chromedriver.chromium.org/downloads
    
    4.2 Extract the downloaded file and place chromedriver under the **drivers/** folder

    4.3 Update the path in conftest.py if needed:     
    ```bash
    chromedriver_path = "./drivers/chromedriver"
    ```

    4.4 Make chromedriver executable, if you are Mac user: 
    chmod +x /Users/<your_user>/drivers/chromedriver

5. **Execution**
    ```bash
    pytest -v
    ```

## Contact
- Author: Onur Ozgur
- Email: onurozgur4@icloud.com
- LinkedIn: [onurrozgurr](https://www.linkedin.com/in/onurrozgurr/)