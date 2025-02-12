from .base_page import BasePage
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()

class LoginPage(BasePage):
    
    # Locators
    USERNAME_FIELD = (By.XPATH, "/html/body/div/div/main/div/div/div/div[2]/form/div/div[1]/input")
    PASSWORD_FIELD = (By.XPATH, "/html/body/div/div/main/div/div/div/div[2]/form/div/div[2]/span/input")
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[2]/form/button')
    WELCOME_MESSAGE = (By.XPATH, "//span[@class='text-white text-2xl font-bold']")
    ERROR_MESSAGE = (By.XPATH,"//div[@class='ant-notification-notice ant-notification-notice-error ant-notification-notice-closable']")
    URL = "https://digitreedev.shorthills.ai/auth/login"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.URL)
        driver.maximize_window()

    # Actions
    def enter_username(self, username):
        self.enter_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.wait_for_element_to_be_clickable(self.LOGIN_BUTTON)
        self.click(self.LOGIN_BUTTON)

    def get_welcome_message(self):
        return self.get_element_text(self.WELCOME_MESSAGE)
    
    def get_error_message(self):
        return self.get_element_text(self.ERROR_MESSAGE)

    #def get_error_message(self):
     #   return self.get_element_text(self.ERROR_MESSAGE)

    def login(self, username_1, password):
        """Combination method to perform login"""
        # username_1 = os.getenv("USERNAME_ENV")
        # print(username_1)
        # password = os.getenv("PASSWORD_ENV")
        # print(password)
        
        self.enter_username(username_1)
        self.enter_password(password)
        self.click_login()