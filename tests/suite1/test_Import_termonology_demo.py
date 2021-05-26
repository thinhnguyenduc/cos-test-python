from selenium.webdriver.common.by import By

from src.utils import logger, common
from tests.suite1.base_suite1 import BaseSuite1


class TestCase1(BaseSuite1):
    ICON = (By.CSS_SELECTOR, "a[href='#!/administration']")
    ABC = (By.CSS_SELECTOR, "[ng-if='access.terminology']")

    def test_case_description(self):
        logger.info("1. Go to Administration Page")
        common.sleep(3)
