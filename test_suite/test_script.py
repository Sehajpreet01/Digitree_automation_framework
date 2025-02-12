from pages.login_page import LoginPage
from selenium import webdriver
import time
from tests.test_login_page import TestLoginPage

# Initialize WebDriver
driver = None
try:
    driver = webdriver.Chrome()  # Specify path if needed
    
    # Create LoginPage instance
    login_page = LoginPage(driver)
    
    # Perform actions
    login_page.login("username", "password")


finally:
    time.sleep(50)
    # Make sure to close the driver even if something goes wrong
    if driver:
        driver.quit()

