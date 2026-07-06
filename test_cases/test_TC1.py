import time
import pytest
from pathlib import Path
import json
from pageObjects.login_page import LoginPage
from utils.excel_reader import ExcelReader

test_data = ExcelReader.read("login_data.xlsx","Sheet1")
@pytest.mark.smoke
@pytest.mark.parametrize("data", test_data)
def test_TC1(browser_instance, data):
    driver = browser_instance
    loginPage = LoginPage( driver )
    print(loginPage.get_title())
    shop_page = loginPage.login( data["userEmail"], data["userPassword"] )
    '''shop_page.add_product_to_cart( data["productName"] )
    print( shop_page.get_title())
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address( "ind" )
    checkout_confirmation.validate_order()'''