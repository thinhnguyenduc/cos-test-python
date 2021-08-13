import builtins

from src.consts import consts
from src.utils import logger, browser_driver, json_util
from tests.form import BaseTestForm


class TCUserPermissions(BaseTestForm):
    """
    Description: Verify user permissions
    """

    def test(self):
        try:
            # Start test
            data_json_file = consts.PROJECT_ROOT + "/data/data.json"
            data = json_util.load(data_json_file)
            logger.info(data["aaa"])
            logger.info(data["ccc"]["ddd"])
            logger.info(data["fff"][0]["f2"])
            # logger.debug(self.driver.title)
            # firefox_driver = browser_driver.create_firefox_driver()
            # firefox_driver.get(builtins.url)
            # End test
        except Exception as ex:
            logger.error(ex)
            self.failures.append(ex)
        finally:
            self.screenshot_binary_data.append(self.save_screenshot())
