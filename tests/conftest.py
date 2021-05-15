import builtins
import logging

import pytest
from selenium.webdriver.common.by import By

from src.consts import consts
from src.utils import logger, create_new_handler_logger, file_util, common
from src.utils.browser_driver import create_chrome_driver
from src.utils.element import wait_for_element_displayed, find_element


@pytest.fixture(scope="session")
def before_all_tests(request):  # Before all tests, run this function one time only.
    print("\x00")  # print a non-printable character to break a new line on console
    logger.info("=== Start Pytest session ===")

    # Init Chrome driver
    driver = create_chrome_driver()
    builtins.driver = driver

    # Navigate to test site
    driver.get("https://cos2-ci.it-development.com/standard/#!/identity/login")
    # Wait until the User ID input displays
    wait_for_element_displayed((By.XPATH, "//input[@placeholder='User ID']"))
    # Enter user credential
    find_element((By.XPATH, "//input[@placeholder='User ID']")).send_keys("sonle")
    find_element((By.XPATH, "//input[@placeholder='Password']")).send_keys("Aaaa!111")
    find_element((By.XPATH, "//button[text()='Sign me in']")).click()
    # Wait a little time to observe
    common.sleep(5)


def pytest_sessionfinish():
    # Quit Chrome driver
    if hasattr(builtins, "driver"):
        getattr(builtins, "driver").quit()
    logger.info("=== End Pytest session ===")
