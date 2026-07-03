import allure
from selenium.webdriver.common.by import By

from utils.browser_utils import BrowserUtils
from pageObjects.shop import ShopPage

class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        #self.driver=driver
        self.username_input = (By.ID, "username")
        self.password = (By.NAME, "password")
        self.sign_button = (By.ID, "signInBtn")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.sign_button).click()
        shop_page = ShopPage(self.driver)
        allure.attach(self.driver.get_screenshot_as_png(),
        name="After Login",
        attachment_type=allure.attachment_type.PNG)
        return shop_page
