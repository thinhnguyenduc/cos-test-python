from src.consts import consts
from src.pages.terminology.import_entity_page import Import_entity_page
from src.utils import common
from tests.master_test import MasterTest


class TC3022(MasterTest):
    def test_case_01_import_site_widget(self):
        entity = Import_entity_page()
        entity.click_on_icon_admin()
        entity.click_on_form_designer_link()
        common.sleep(2)  # have to sleep ????

        entity.click_on_row_on_search_result()
        common.sleep(2)
        entity.click_on_icon_humberger()
        entity.click_on_button_new()
        common.sleep(2)
        entity.clicK_on_entity_on_dropdown_list()
        #waiting for report form shows
        common.sleep(2)

        entity.select_on_target_entity_dropdownlist("Site")
        csv_file = consts.PROJECT_ROOT + "/data/import_site_widget.csv"
        entity.select_file_csv(csv_file)
        common.sleep(2)
        entity.select_operation("Update only")

        common.sleep(2)
        self.link_to_prefix(entity)
        self.link_to_id(entity)

    pass

    def link_to_id(self, entity: Import_entity_page):
        entity.click_on_map_id()
        entity.enter_prefix_on_search("WO - ID - number")
        entity.click_on_item_on_autocomplete()
        entity.click_on_map_prefix_icon()
        entity.click_on_ok_button_on_popup()
        pass

    def link_to_prefix(self, entity: Import_entity_page):
        entity.click_on_map_prefix()
        entity.enter_prefix_on_search("WO - ID - prefix")
        entity.click_on_item_on_autocomplete()
        entity.click_on_map_prefix_icon()
        entity.click_on_ok_button_on_popup()
        pass

pass
