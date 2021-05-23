import os
from datetime import time
from random import random, randint

from selenium.webdriver.common.by import By

from src.utils import logger, common
from src.utils.element import find_element, find_element_present, wait_for_element_displayed
from tests.suite1.base_suite1 import BaseSuite1


class TestCase1(BaseSuite1):

    ICON = (By.CSS_SELECTOR, "a[href='#!/administration']")
    ABC = (By.CSS_SELECTOR, "[ng-if='access.terminology']")

    def test_case_description(self):
        logger.info("1. Go to Administration Page")
        find_element(self.ICON).click()

        logger.info("2. Go to Terminology Editor.")
        find_element(self.ABC).click()
        # Wait a little time to observe
        logger.info("3. Click on the right button")
        find_element((By.CSS_SELECTOR, "div.pull-right button")).click()

        logger.info("4. Click on the Import button")
        find_element((By.CSS_SELECTOR, "[href = '#!/terminology/import/0']")).click()

        logger.info("5.Upload file ")
        csv_file = os.path.dirname(os.getcwd()) + "/data/import1level.csv"
        logger.debug(f"------CSV file: {csv_file}")
        find_element((By.CSS_SELECTOR, "input[type=file]")).send_keys(csv_file)

        logger.info("6.Enter Terminology Name")
        # name_terminology = "ter" + str(randint(1, 101))
        common.sleep(5)
        #
        # #input[name=terminology_name]
        #
        # sleep(50)
        # find_element(By.CSS_SELECTOR, "input[name=terminology_name]").send_keys(
        #     name_terminology)
        #
        # resource_terminology = "ter" + str(randint(1, 101))
        #
        # logger.info("7.Enter Terminology Resource")
        # wait_for_element_displayed((By.CSS_SELECTOR, "[ng-model='import.terminology.resource_name']")).send_keys(
        #     resource_terminology)
        #
        # logger.info("8. Map Field")
        # find_element((By.CSS_SELECTOR, "[ng-model='import.parsingProperties.header']")).click()
        # fullstring = find_element((By.CSS_SELECTOR, "div.col-md-1 div.icheckbox_minimal-blue")).get_property("class")
        # print("------------" + fullstring)
        #
        # if fullstring.find("checked") == -1:
        #     logger.info(" Check header checkbox")
        #     find_element((By.CSS_SELECTOR, "div.col-md-1 div.icheckbox_minimal-blue")).click();
        #
        # # div.col-md-1 div.icheckbox_minimal-blue
        # # div.icheckbox_minimal - blue.checked
        # time.sleep(2)
        #
        # logger.info(f"Title: {self.driver.title}")
        # assert self.driver.title == "ClickOnSite"
