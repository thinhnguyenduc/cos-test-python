import builtins
import unittest

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from src.utils import logger


@pytest.mark.usefixtures("before_all_tests")
class MasterTest(unittest.TestCase):

    def setUp(self):  # Before each test case
        self.driver: WebDriver = getattr(builtins, "driver")
        self.test_case_name = self.__class__.__name__.lower()
        logger.info(f"Start test case: {self.test_case_name}")

    def tearDown(self):  # After each test case
        logger.info(f"End test case: {self.test_case_name}")
