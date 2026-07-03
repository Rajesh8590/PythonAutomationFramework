from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser_utils import BrowserUtils

class AutomationPracticePage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.phoneview=(By.XPATH, "//b[text()='iphone 13 pro']/../..//button[text()=' View']")
        self.continueButton=(By.CLASS_NAME, "continue")
        self.fashionCheckbox=(By.XPATH, "(//label[text()='fashion'])[2]/..//input[@type='checkbox']")

    def click_on_phoneView(self):
        #wait=WebDriverWait(self.driver,10)
        #wait.until(EC.element_to_be_clickable(self.phoneview))
        self.driver.find_element(*self.phoneview).click()

    def verify_phoneClicked(self):
        assert self.driver.find_element(*self.continueButton).is_displayed()

    def click_Checkbox(self):
        self.driver.find_element(*self.fashionCheckbox).click()
    
    def verify_checkboxClicked(self):
        assert self.driver.find_element(*self.fashionCheckbox).is_selected()