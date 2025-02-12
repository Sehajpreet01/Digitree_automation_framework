import unittest
import os
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.driver_manager import DriverManager
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.upload_your_file_page import UploadFile
from dotenv import load_dotenv
import time
import pyautogui

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
        self.upload_your_file_page = UploadFile(self.driver)

        # Log in before running home page tests
        username = os.getenv("USERNAME_ENV")
        password = os.getenv("PASSWORD_ENV")
        self.login_page.login(username, password)

        # Ensure login was successful
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.home_page.HOME_PAGE_IDENTIFIER)  # Adjust selector as needed
        )
        logging.info("Successfully logged in and navigated to Home Page.")
        
    def test_click_upload(self):
        """Test upload image button working fine"""
        self.home_page.click_upload_image()

        successmessage = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.home_page.SUCCESSMESSAGE)).text
        
        self.assertEqual(successmessage, "Upload Your File", "Welcome message is incorrect.")

        self.assertNotEqual(self.driver.current_url, HomePage.URL, "Login failed: URL did not change after login.")

    def test_browse_button_present(self):
        """Test browse button present or not"""
        self.home_page.click_upload_image()
        self.upload_your_file_page.get_browser_text()

        browser_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.upload_your_file_page.BROWSER_BUTTON)).text
        
        self.assertEqual(browser_button, "Browse", "Button is not present bug logged.")

    def test_submit_button_present(self):
        """Test submit button present or not"""
        self.home_page.click_upload_image()
        self.upload_your_file_page.get_submit_button()

        submit_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.upload_your_file_page.SUBMIT_BUTTON)).text

        self.assertEqual(submit_button, "Submit", "Submit button is not present.")

    def test_browse_file(self):
        """Test file upload functionality using the Browse button"""
        self.home_page.click_upload_image()

        file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.upload_your_file_page.BROWSER_INPUT)
        )

        file_path = os.path.abspath("Assests/sample_image.png") 
        assert os.path.exists(file_path), f"File not found: {file_path}"

        file_input.send_keys(file_path)

        # time.sleep(10)

        successmessage = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.upload_your_file_page.UPLOADSUCESSMESSAGE)).text

    def test_submit_button(self):
        """Test the submit button functionality and ensure the URL changes after submission."""

        # Click the upload image button to open the upload page
        self.home_page.click_upload_image()

        # Wait for the file input to be present and upload the file
        file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.upload_your_file_page.BROWSER_INPUT)
        )

        file_path = os.path.abspath("Assests/sample_image.png") 
        assert os.path.exists(file_path), f"File not found: {file_path}"
        file_input.send_keys(file_path)

        # Wait for the submit button to become clickable
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.upload_your_file_page.SUBMIT_BUTTON)
        )
        
        # Verify that the submit button is enabled after the file upload
        self.assertTrue(submit_button.is_enabled(), "Submit button is not enabled after file upload.")
        
        # Click the submit button
        submit_button.click()

        # Wait for the URL to change after the form submission
        WebDriverWait(self.driver, 10).until(
            EC.url_changes(self.driver.current_url)
        )

        # Capture the new URL after the button click
        new_url = self.driver.current_url
        logging.info(f"New URL after submitting: {new_url}")

        # Assert that the URL has changed (it should no longer be the home page URL)
        self.assertNotEqual(self.driver.current_url, HomePage.URL, "URL did not change after submitting.")


    def test_invalid_file_format(self):
        """Test that only jpg, jpeg, and png files enable the submit button, others should not."""

        self.home_page.click_upload_image()

        file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.upload_your_file_page.BROWSER_INPUT)
        )

        invalid_files = [
            "Assests/sample_document.pdf",
            "Assests/sample_excel.xlsx",
            "Assests/sample_csv.csv"
        ]

        for file in invalid_files:
            file_path = os.path.abspath(file)
            assert os.path.exists(file_path), f"File not found: {file_path}"

            file_input.send_keys(file_path)

            # Wait and check if the submit button is enabled
            submit_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.upload_your_file_page.SUBMIT_BUTTON)
            )

            self.assertFalse(submit_button.is_enabled(), f"Submit button should be disabled for {file}")

        # Now test with a valid image file
        valid_file_path = os.path.abspath("Assests/sample_image.png")
        assert os.path.exists(valid_file_path), f"File not found: {valid_file_path}"

        file_input.send_keys(valid_file_path)

        # Wait and check if the submit button is enabled
        submit_button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.upload_your_file_page.SUBMIT_BUTTON)
        )

        self.assertTrue(submit_button.is_enabled(), "Submit button should be enabled for valid image files.")


    def test_large_image_file(self):
        """Test that a single jpeg, jpg, or png file exceeding 1MB prevents submission and does not change URL."""

        self.home_page.click_upload_image()

        file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.upload_your_file_page.BROWSER_INPUT)
        )

        # Provide path to a large image file (>1MB)
        large_file_path = os.path.abspath("Assests/sample1MB.png")
        
        assert os.path.exists(large_file_path), f"File not found: {large_file_path}"
        assert os.path.getsize(large_file_path) > 1 * 1024 * 1024, "File size should be greater than 1MB"

        file_input.send_keys(large_file_path)

        # Capture current URL before submission attempt
        current_url = self.driver.current_url

        # Wait for submit button to be present and attempt to click
        submit_button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.upload_your_file_page.SUBMIT_BUTTON)
        )

        submit_button.click()

        time.sleep(5)  # Give time to process

        # Capture the new URL after clicking
        new_url = self.driver.current_url

        # **Test should pass if the URL has NOT changed**
        assert new_url == current_url, "Test Failed: URL changed when it should not have."

        logging.info("✅ Test passed: Large image file upload is correctly restricted.")