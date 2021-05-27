import allure

from src.utils import logger, common
from tests.suite1.base_suite1 import BaseSuite1


class TestCaseDemo(BaseSuite1):

    @allure.title("Import Terminology")
    def test_case_description(self):
        try:
            # Start test
            logger.info("1. Go to Administration Page")
            common.sleep(3)
            assert False
            # End test
        except Exception as ex:
            logger.error(ex)
            self.failures.append(ex)
        finally:
            self.screenshot_binary_data.append(self.save_screenshot())
