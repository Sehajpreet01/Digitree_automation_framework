from .base_page import BasePage
from selenium.webdriver.common.by import By

class UploadFile(BasePage):
    # Locators
    UPLOAD_IMAGE_BUTTON = (By.XPATH, "//span[normalize-space()='+ Upload Image']")
    BROWSER_BUTTON = (By.XPATH,"//label[normalize-space()='Browse']")
    SUBMIT_BUTTON = (By.XPATH,"/html/body/div[1]/div/main/div/div/div[2]/div/div/button")
    HOME_BUTTON = (By.XPATH,"//a[normalize-space()='Home']")
    USER_NAME_ = (By.XPATH,"//span[@class='ant-dropdown-trigger flex items-center text-white cursor-pointer mr-12 text-lg space-x-2 hover:brightness-50']")
    LOGOUT_BUTTON = (By.XPATH,"//li[@role='menuitem']")
    UPLOADSUCESSMESSAGE = (By.XPATH,"//div[@class='ant-notification-notice ant-notification-notice-success ant-notification-notice-closable']")
    BROWSER_INPUT = (By.XPATH,'//*[@id="root"]/div/main/div/div/div[2]/div/div/div/input[@type="file"]')

    URL = "https://digitreedev.shorthills.ai/dashboard/upload"

    def __init__(self, driver):
            super().__init__(driver)
            self.driver.get(self.URL)

    #Actions:

    def click_browser_button(self):
        self.click(self.BROWSER_BUTTON)

    def click_browser_input_presence(self):
        self.is_element_present(self.BROWSER_INPUT)

    def get_browser_text(self):
         self.get_element_text(self.BROWSER_BUTTON)

    def click_submit_button(self):
        self.click(self.SUBMIT_BUTTON)

    def get_submit_button(self):
         self.get_element_text(self.SUBMIT_BUTTON)

    def click_home_button(self):
         self.click(self.HOME_BUTTON)

    def click_user_name(self):
         self.click(self.USER_NAME_)

    def get_user_name(self):
         self.get_element_text(self.USER_NAME_)

    def click_logout_button(self):
         self.click(self.LOGOUT_BUTTON)

    def get_upload_text(self):
        return self.get_element_text(self.UPLOADSUCESSMESSAGE)
   