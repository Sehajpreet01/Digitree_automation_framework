from .base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    # Locators
    UPLOAD_IMAGE_BUTTON = (By.XPATH, "//span[normalize-space()='+ Upload Image']")
    EDIT_TREE_BUTTON = (By.XPATH, "//td[@class='ant-table-cell ant-table-cell-row-hover']//button[2]")
    VIEW_TREE_BUTTON = (By.XPATH, "//td[@class='ant-table-cell ant-table-cell-row-hover']//div[@class='flex space-x-2']//button[1]")
    PAGINATION_1 = (By.XPATH, "//a[normalize-space()='1']")
    PAGINATION_2 = (By.XPATH, "//a[normalize-space()='2']")
    SNO = (By.XPATH, "//span[normalize-space()='S. No']")
    IMAGEID = (By.XPATH, "//span[normalize-space()='Image ID']")
    PROCESSEDON = (By.XPATH, "//span[normalize-space()='Processed On']")
    LASTUPDATED = (By.XPATH, "//span[normalize-space()='Last Updated']")
    EDITEDBY = (By.XPATH, "//span[normalize-space()='Edited By']")
    NUMBEROFVERSIONS = (By.XPATH, "//span[normalize-space()='Number of Versions']")
    ACTION = (By.XPATH, "//span[normalize-space()='Action']")
    SUCCESSMESSAGE = (By.XPATH,'/html/body/div/div/main/div/div/div[2]/div/div/h2')
    HOME_PAGE_IDENTIFIER = (By.XPATH, "//span[@class='text-white text-2xl font-bold']")
    PREVIOUS_BUTTON_EDITTREE = (By.XPATH,"//span[normalize-space()='Previous']")

    URL = "https://digitreedev.shorthills.ai/dashboard/home"  # Replace with the actual URL of the home page

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.URL)

    # Actions
    def click_upload_image(self):
        self.click(self.UPLOAD_IMAGE_BUTTON)

    def click_edit_tree(self):
        self.click(self.EDIT_TREE_BUTTON)

    def click_view_tree(self):
        self.click(self.VIEW_TREE_BUTTON)

    def click_pagination_1(self):
        self.click(self.PAGINATION_1)

    def click_pagination_2(self):
        self.click(self.PAGINATION_2)

    def get_sno_text(self):
        return self.get_element_text(self.SNO)

    def get_image_id_text(self):
        return self.get_element_text(self.IMAGEID)

    def get_processed_on_text(self):
        return self.get_element_text(self.PROCESSEDON)

    def get_last_updated_text(self):
        return self.get_element_text(self.LASTUPDATED)

    def get_edited_by_text(self):
        return self.get_element_text(self.EDITEDBY)

    def get_number_of_versions_text(self):
        return self.get_element_text(self.NUMBEROFVERSIONS)

    def get_action_text(self):
        return self.get_element_text(self.ACTION)
    
    def get_upload_text(self):
        return self.get_element_text(self.SUCCESSMESSAGE)
    
    def get_welcome_message(self):
        return self.get_element_text(self.HOME_PAGE_IDENTIFIER)
    
    def get_save_button(self):
        return self.get_element_text(self.PREVIOUS_BUTTON_EDITTREE)
