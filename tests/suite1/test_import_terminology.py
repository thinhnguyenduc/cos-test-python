from random import randint

from selenium.webdriver.common.by import By

from src.consts import consts
from src.utils import logger, common
from src.utils.element import find_element
from tests.suite1.base_suite1 import BaseSuite1


class WebSyncCreateCollection(BaseSuite1):
    ICON = (By.CSS_SELECTOR, "a[href='#!/administration']")
    TERMINOLOGY_EDITOR = (By.CSS_SELECTOR, "[ng-if='access.terminology']")
    TERMINOLOGY_NAME = (By.CSS_SELECTOR, "input[name=terminology_name]")
    TERMINOLOGY_RESOURCE = (By.CSS_SELECTOR, "[ng-model='import.terminology.resource_name']")
    HEADER_CHECKBOX = (By.CSS_SELECTOR, "[for='header'] + div")
    LEVEL_IMPORT_1 = (By.CSS_SELECTOR, "[name = 'import_parsing_max_levels']")
    MAP_ICON = (By.CSS_SELECTOR, ".table-header a")
    BUTTON_RUN = (By.CSS_SELECTOR, ".btn-success")
    LINK_NEW_TER = (By.CSS_SELECTOR, ".list-horizontal a")
    BUTTON_CANCEL = (By.CSS_SELECTOR, ".content-actionbar a")

    TERMINOLOGY_NAME_DETAIL = (By.CSS_SELECTOR, ".content-header .ng-binding")
    TERMINOLOGY_RESOURCE_NAME_DETAIL = (By.CSS_SELECTOR, "[name='resource_name']")
    SEARCH_TERMINOLOGY_INTERNAL_TEXTBOX = (By.CSS_SELECTOR, ".content-searchbox-input")
    DELETE_ICON = (By.CSS_SELECTOR, ".hover-buttons-td")

    def test_case_01_import1level(self):
        logger.info("1. Go to Administration Page")
        find_element(self.ICON).click()

        logger.info("2. Go to Terminology Editor.")
        find_element(self.TERMINOLOGY_EDITOR).click()

        logger.info("3. Click on the right button")
        find_element((By.CSS_SELECTOR, "div.pull-right button")).click()

        logger.info("4. Click on the Import button")
        find_element((By.CSS_SELECTOR, "[href = '#!/terminology/import/0']")).click()

        logger.info("5. Upload file ")
        csv_file = consts.PROJECT_ROOT + "/data/import1level.csv"
        find_element((By.CSS_SELECTOR, "input[type=file]")).send_keys(csv_file)

        logger.info("6.Enter Terminology Name")
        name_terminology = "ter" + str(randint(1, 101))
        find_element(self.TERMINOLOGY_NAME).send_keys(name_terminology)
        common.sleep(5)

        resource_terminology = "ter" + str(randint(1, 101))
        logger.info("7. Enter Terminology Resource")
        logger.debug({resource_terminology})
        find_element(self.TERMINOLOGY_RESOURCE).send_keys(resource_terminology)

        logger.info("8. MAP ")
        common.sleep(5)
        # find_element(self.HEADER_CHECKBOX).click()
        # = find_element(self.HEADER_CHECKBOX).get_attribute("class")
        logger.info("9.Enter to max level ")
        find_element(self.LEVEL_IMPORT_1).send_keys("1")

        logger.info("10. Click# on Map icon ")
        find_element(self.MAP_ICON).click()

        logger.info("11. Click Run button ")
        find_element(self.BUTTON_RUN).click()

        logger.info("12. Click Show Terminology to navigate to terminology ")
        find_element(self.LINK_NEW_TER).click()

        logger.info("13. Verify Terminology Name")
        logger.debug(find_element(self.TERMINOLOGY_NAME_DETAIL).text)
        assert find_element(self.TERMINOLOGY_NAME_DETAIL).text == name_terminology

        logger.info("14. Click on Cancel button to back on Entity list of Terminology")
        find_element(self.BUTTON_CANCEL).click()
        logger.info("15. Search with terminology name")
        find_element(self.SEARCH_TERMINOLOGY_INTERNAL_TEXTBOX).click()
        logger.info("16. Delete with terminology above")
        find_element(self.DELETE_ICON).click()
