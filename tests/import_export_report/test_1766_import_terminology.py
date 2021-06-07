from random import randint

from src.consts import consts
# from src.pages.terminology.import_terminology_page import ImportTerminologyPage
from src.pages.terminology.import_terminology_page import ImportTerminologyPage
from src.utils import logger, common
from src.utils.element import find_element, send_keys
from tests.master_test import MasterTest


class TC1766(MasterTest):

    def test_case_01_import_1_level(self):
        import_terminology_page = ImportTerminologyPage()
        # Roi gio bi gi ne?
        import_terminology_page.click_on_administrator_icon()
        import_terminology_page.click_on_terminology_editor()
        import_terminology_page.click_on_action_button()
        import_terminology_page.click_on_import_on_dropdown_list()
        common.sleep(2)

        csv_file = consts.PROJECT_ROOT + "/data/import1level.csv"
        name_terminology = "ter" + str(randint(50, 1001))

        import_terminology_page.enter_name(name_terminology)
        import_terminology_page.enter_resource_name(name_terminology)
        import_terminology_page.enter_csv_file(csv_file)
        import_terminology_page.click_map_icon()
        import_terminology_page.click_on_run_button()
        import_terminology_page.click_on_show_terminology()
        import_terminology_page.verify_terminology_name()
        import_terminology_page.click_on_cancel_button()
        # End page object

        self.delete_terminology(name_terminology)
        common.sleep(5)

    def create_terminology(self, name_terminology: ImportTerminologyPage):
        resource_terminology = "ter" + str(randint(50, 1001))
        logger.info("7. Enter Terminology Resource")
        logger.debug({resource_terminology})
        find_element(self.TERMINOLOGY_RESOURCE)
        send_keys(self.TERMINOLOGY_RESOURCE, name_terminology, False, False)

        logger.info("9.Enter to max level ")
        element_level = find_element(self.LEVEL_IMPORT_1)
        element_level.clear()
        element_level.send_keys("1")

        logger.info("10. Click# on Map icon ")
        find_element(self.MAP_ICON).click()

        logger.info("11. Click Run button ")
        find_element(self.BUTTON_RUN).click()

        logger.info("12. Click Show Terminology to navigate to terminology ")
        find_element(self.LINK_NEW_TER).click()

        logger.info("13. Verify Terminology Name")
        logger.debug(find_element(self.TERMINOLOGY_NAME_DETAIL).text)
        assert find_element(self.TERMINOLOGY_NAME_DETAIL).text == name_terminology


    def delete_terminology(self, name_terminology):
        logger.info("15. Enter terminology on search text box")
        search_textbox = find_element(self.SEARCH_TERMINOLOGY_INTERNAL_TEXTBOX)
        search_textbox.clear()
        search_textbox.send_keys(name_terminology)

        logger.info("15. Search with terminology name")
        find_element(self.SEARCH_TERMINOLOGY_INTERNAL_TEXTBOX).click()

        logger.info("16. Delete with terminology above")
        find_element(self.DELETE_ICON).click()

        logger.info("17. Display a popup message and click on Delete button")
        find_element(self.BUTTON_CANCEL_MODEL).click()
