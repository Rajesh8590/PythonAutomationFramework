import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.config_reader import ConfigReader
from utils.logger import Logger

logger = Logger.get_logger()
config = ConfigReader.get_config()

def pytest_addoption(parser):
    parser.addoption("--browser_name",action="store",default=config["browser"])

@pytest.fixture(scope="function")
def browser_instance(request):
    test_name = request.node.name
    logger.info("=" * 70)
    logger.info(f"TEST CASE STARTED : {test_name}")
    logger.info("=" * 70)
    logger.info(f"========== {request.node.name} Started ==========")
    browser_name = request.config.getoption("--browser_name")
    logger.info(f"Launching {browser_name} Browser")
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")

    service = Service()
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service,options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    driver.maximize_window()
    logger.info(f"Opening URL : {config['url']}")
    driver.get(config["url"])
    driver.implicitly_wait(int(config["timeout"]))
    yield driver
    driver.quit()
    logger.info(f"========== {request.node.name} Finished ==========")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser_instance")
        if driver:
            allure.attach(driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )