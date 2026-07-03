from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def enter_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def is_displayed(self, locator):
        assert self.driver.find_element(*locator).is_displayed()

    def select_static_dropdown(self, *locator, value):
        select_dropdown = Select(self.driver.find_element(*locator))
        select_dropdown.select_by_value(value)

    def select_dynamic_dropdown(self, *locator, value):
        dropdown_options = self.driver.find_elements(*locator)
        for option in dropdown_options:
            if option.text == value:
                option.click()
                break

    def select_checkbox(self,*locator, value):
        checkboxes = self.driver.find_elements(*locator)
        for checkbox in checkboxes:
            if checkbox.get_attribute("value") == value:
                checkbox.click()
                break

    def select_radio_button(self,*locator, value):
        radio_buttons = self.driver.find_elements(*locator)
        for radio_button in radio_buttons:
            if radio_button.get_attribute("value") == value:
                radio_button.click()
                break