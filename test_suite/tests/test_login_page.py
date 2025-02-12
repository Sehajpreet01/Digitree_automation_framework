import unittest
import os
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.driver_manager import DriverManager
from pages.login_page import LoginPage
import time
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = DriverManager.get_driver(browser='chrome')
        self.login_page = LoginPage(self.driver)

    def test_username_field(self):
        """Test all login page elements are present."""
        self.assertTrue(self.login_page.is_element_present(self.login_page.USERNAME_FIELD), "Username field missing.")

    def test_password_field(self):
        """Test all login page elements are present."""
        self.assertTrue(self.login_page.is_element_present(self.login_page.PASSWORD_FIELD), "Password field missing.")

    def test_login_button(self):
        """Test all login page elements are present."""
        self.assertTrue(self.login_page.is_element_present(self.login_page.LOGIN_BUTTON), "Login button missing.")

    def test_successful_login(self):
        """Test successful login with valid credentials."""
        username = os.getenv("USERNAME_ENV")
        password = os.getenv("PASSWORD_ENV")
        self.login_page.login(username, password)

        welcome_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_page.WELCOME_MESSAGE)
        ).text
        self.assertEqual(welcome_message, "Hello, testuser1", "Welcome message is incorrect.")

        self.assertNotEqual(self.driver.current_url, LoginPage.URL, "Login failed: URL did not change after login.")

    def test_login_with_invalid_credentials(self):
        """Test login with incorrect username and password."""
        self.login_page.login("wronguser", "wrongpassword")

        time.sleep(4)

        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_page.ERROR_MESSAGE)
        ).text
        self.assertIn("User does not exist", error_message, "Error message not displayed for invalid credentials.")
        print('--------------------------', error_message)

    def test_login_with_blank_username(self):
        """Test fails if the user is redirected after leaving the username blank."""
        password = os.getenv("PASSWORD_ENV")
        initial_url = self.driver.current_url

        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_page.PASSWORD_FIELD)
        )
        password_field.clear()
        password_field.send_keys(password)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_page.LOGIN_BUTTON)
        )
        login_button.click()

        new_url = self.driver.current_url
        self.assertEqual(initial_url, new_url, "Test failed: User was redirected after leaving username blank.")

    def test_login_with_blank_password(self):
        """Test login fails when password is left empty."""
        username = os.getenv("USERNAME_ENV")
        initial_url = self.driver.current_url

        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_page.USERNAME_FIELD)
        )
        username_field.clear()
        username_field.send_keys(username)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_page.LOGIN_BUTTON)
        )
        login_button.click()

        new_url = self.driver.current_url
        self.assertEqual(initial_url, new_url, "Test failed: User was redirected after leaving password blank.")

    def test_login_with_uppercase_username(self):
        """Test user can log in with uppercase username and correct password."""
        username = os.getenv("USERNAME_ENV").upper()  # Convert username to uppercase
        password = os.getenv("PASSWORD_ENV")
        self.login_page.login(username, password)

        welcome_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_page.WELCOME_MESSAGE)
        ).text
        self.assertEqual(welcome_message, "Hello, testuser1", "Welcome message is incorrect.")

        self.assertNotEqual(self.driver.current_url, LoginPage.URL, "Login failed: URL did not change after login.")

    def test_login_with_uppercase_password(self):
        """Test user cannot log in with uppercase password."""
        username = os.getenv("USERNAME_ENV")
        password = os.getenv("PASSWORD_ENV").upper()  # Convert password to uppercase
        self.login_page.login(username, password)

        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_page.ERROR_MESSAGE)
        ).text
        self.assertIn("Invalid credentials", error_message, "Error message not displayed for invalid credentials.")
        print('--------------------------', error_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()