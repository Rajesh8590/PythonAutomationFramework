from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from pageObjects.basePage import BasePage

class BrowserUtils(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    def get_title(self):
        return self.driver.title
   
    def wait_for_presence(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator))

    def wait_for_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    def wait_for_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator))
    
    @staticmethod
    def upload_file(element, filename):
        file_path = os.path.abspath(f"resources/uploads/{filename}")
        element.send_keys(file_path)

    '''Usage of the upload file method 
    BrowserUtils.upload_file(
    self.driver.find_element(*self.upload_button),"resume.pdf")'''

    @staticmethod
    def is_file_downloaded(filename):
        file_path = os.path.abspath(f"resources/downloads/{filename}")
        return os.path.exists(file_path)
    
    '''Usage of the upload file method 
    BrowserUtils.upload_file(
    self.driver.find_element(*self.upload_button),"resume.pdf")'''