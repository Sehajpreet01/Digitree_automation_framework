from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    def is_visible(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()

    def is_element_present(self, by_locator):
        """Checks if an element is present in the DOM but not necessarily visible."""
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
            return True
        except:
            return False

    def wait_for_element_to_be_clickable(self, by_locator):
        """Waits until an element is clickable before clicking."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def get_page_title(self):
        """Returns the current page title."""
        return self.driver.title
    
    def scroll_to_element(self, by_locator):
        """Scrolls to the element."""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
