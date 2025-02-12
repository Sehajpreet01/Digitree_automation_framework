import unittest
import os
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.driver_manager import DriverManager
from pages.login_page import LoginPage
from pages.home_page import HomePage
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestHomePage(unittest.TestCase):
    def setUp(self):
        """Setup WebDriver and log in before each test."""
        self.driver = DriverManager.get_driver(browser='chrome')
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)

        # Log in before running home page tests
        username = os.getenv("USERNAME_ENV")
        password = os.getenv("PASSWORD_ENV")
        self.login_page.login(username, password)

        #Ensure login was successful
        WebDriverWait(self.driver, 10).until(
           EC.presence_of_element_located(self.home_page.HOME_PAGE_IDENTIFIER)  # Adjust selector as needed
        )
        logging.info("Successfully logged in and navigated to Home Page.")
    
    def test_click_upload(self):
        "Test upload image button working fine"
        self.home_page.click_upload_image()

        successmessage = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.home_page.SUCCESSMESSAGE)).text
        
        print(successmessage)
        self.assertEqual(successmessage, "Upload Your File", "Welcome message is incorrect.")

        self.assertNotEqual(self.driver.current_url, HomePage.URL, "Login failed: URL did not change after login.")

    def test_click_edit_tree(self):
        "Test edit tree button working fine"
        self.home_page.click_edit_tree()

        savebutton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.home_page.PREVIOUS_BUTTON_EDITTREE)).text
        
        self.assertEqual(savebutton, "Previous", "Welcome message is incorrect.")

        self.assertNotEqual(self.driver.current_url, HomePage.URL, "Login failed: URL did not change after login.")
    
    def test_click_view_tree(self):
        "Test view tree button working fine"
        initial_url = self.driver.current_url

        self.home_page.click_view_tree()

        new_url = self.driver.current_url

        self.assertEqual(initial_url, new_url, "Test failed: User was not redirected after clicking view tree.")

    def test_click_pagination_2(self):
        "Test edit tree button working fine"
        self.home_page.click_pagination_2()

        homepage_identify = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.home_page.SNO)).text
        
        self.assertEqual(homepage_identify, "S. No", "Pagination worked fine")

    def test_click_pagination_1(self):
        "Test edit tree button working fine"
        self.home_page.click_pagination_1()

        homepage_identify = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.home_page.SNO)).text
        
        self.assertEqual(homepage_identify, "S. No", "Pagination worked fine")
    
    def test_sno(self):
        "Test edit tree button working fine"
        self.home_page.get_sno_text()

        homepage_identify = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.home_page.SNO)).text
        
        self.assertEqual(homepage_identify, "S. No", "Name does not match with column")
    
    def test_image_id(self):
        "Test edit tree button working fine"
        self.home_page.get_image_id_text()

        homepage_image_id = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.home_page.IMAGEID)).text
        
        self.assertEqual(homepage_image_id, "Image ID", "Name does not match with column")
    
    def test_processed_on(self):
        "Test edit tree button working fine"
        self.home_page.get_processed_on_text()

        homepage_image_id = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.home_page.PROCESSEDON)).text
        
        self.assertEqual(homepage_image_id, "Processed On", "Name does not match with column")
    
    def test_last_updated(self):
        "Test edit tree button working fine"
        self.home_page.get_last_updated_text()

        homepage_image_id = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.home_page.LASTUPDATED)).text
        
        self.assertEqual(homepage_image_id, "Last Updated", "Name does not match with column")
    
    def test_edited_by(self):
        "Test edit tree button working fine"
        self.home_page.get_edited_by_text()

        homepage_image_id = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.home_page.EDITEDBY)).text
        
        self.assertEqual(homepage_image_id, "Edited By", "Name does not match with column")

    def test_number_of_versions(self):
        "Test edit tree button working fine"
        self.home_page.get_number_of_versions_text()

        homepage_image_id = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.home_page.NUMBEROFVERSIONS)).text
        
        self.assertEqual(homepage_image_id, "Number of Versions", "Name does not match with column")

    def test_action(self):
        "Test edit tree button working fine"
        self.home_page.get_action_text()

        homepage_image_id = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.home_page.ACTION)).text
        
        self.assertEqual(homepage_image_id, "Action", "Name does not match with column")

    
    def tearDown(self):
        """Close the browser after each test."""
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
