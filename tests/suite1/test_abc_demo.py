from src.utils import logger
from tests.suite1.base_suite1 import BaseSuite1


class TestCase1(BaseSuite1):

    def test_case_description(self):
        logger.info(". Step 1")
        logger.info(". Step 2")
        logger.info(". Step 3")
        logger.info(f"Title: {self.driver.title}")
        assert self.driver.title == "ClickOnSite"
