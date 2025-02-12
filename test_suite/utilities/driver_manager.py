# utilities/driver_manager.py
from selenium import webdriver

class DriverManager:
    @staticmethod
    def get_driver(browser="chrome"):
        if browser == "chrome":
            return webdriver.Chrome()
        elif browser == "firefox":
            return webdriver.Firefox()
        elif browser =="edge":
            return webdriver.Edge()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

    @staticmethod
    def quit_driver(driver):
        if driver:
            driver.quit()