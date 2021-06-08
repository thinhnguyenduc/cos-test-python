from random import randint

from src.consts import consts
# from src.pages.terminology.import_terminology_page import ImportTerminologyPage
from src.pages.terminology.import_terminology_page import ImportTerminologyPage
from src.utils import logger, common
from tests.master_test import MasterTest


class TC1766(MasterTest):

    def a_test_case_01_import_1_level(self):
        terminology = ImportTerminologyPage()
        terminology.click_on_administrator_icon()
        csv_file = consts.PROJECT_ROOT + "/data/import1level.csv"
        name_terminology = "ter" + str(randint(50, 1001))
        self.go_to_terminology_page(terminology)
        self.create_terminology(name_terminology, csv_file, terminology)
        self.delete_terminology(name_terminology, terminology)
        #  common.sleep(10)
        pass

    def go_to_terminology_page(self, terminology: ImportTerminologyPage):
        terminology.click_on_terminology_editor()
        terminology.click_on_action_button()
        terminology.click_on_import_on_dropdown_list()
        # common.sleep(12) #have to wait need improvement
        # S terminology.verify_import_form_is_loaded()
        pass

    def create_terminology(self, name_terminology, csv_file, terminology: ImportTerminologyPage):
        common.sleep(2)
        terminology.enter_name(name_terminology)
        #  terminology.enter_resource_name(name_terminology)
        terminology.enter_csv_file(csv_file)
        terminology.click_map_icon()
        terminology.click_on_run_button()
        terminology.click_on_show_terminology()
        terminology.verify_terminology_name(name_terminology)
        terminology.click_on_cancel_button()
        pass

    def delete_terminology(self, name_terminology, terminology: ImportTerminologyPage):
        logger.info("15. Enter terminology on search text box")
        common.sleep(5)
        terminology.enter_name_on_internal_textbox(name_terminology)
        terminology.click_on_delete_icon()
        terminology.click_on_button_cancel_on_model()

    def test_case_02_import_2_level(self):
        terminology = ImportTerminologyPage()
        terminology.click_on_administrator_icon()
        csv_file = consts.PROJECT_ROOT + "/data/import2level.csv"
        name_terminology = "ter" + str(randint(50, 1001))
        self.go_to_terminology_page(terminology)
        self.create_terminology_2level(name_terminology, csv_file, terminology)
        self.delete_terminology(name_terminology, terminology)
        #  common.sleep(10)
        pass

    def create_terminology_2level(self, name_terminology, csv_file, terminology: ImportTerminologyPage):
        common.sleep(2)
        terminology.enter_name(name_terminology)
        terminology.enter_deep("2")
        terminology.enter_csv_file(csv_file)
        terminology.click_map_icon()
        terminology.click_on_run_button()
        terminology.click_on_show_terminology()
        terminology.verify_terminology_name(name_terminology)
        terminology.click_on_cancel_button()
        pass
