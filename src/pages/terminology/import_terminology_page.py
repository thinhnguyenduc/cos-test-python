from selenium.webdriver.common.by import By

from src.utils import logger
from src.utils.element import send_keys, find_element


def click_on_action_button():
    logger.info("3. Click on the action button")
    find_element((By.CSS_SELECTOR, "div.pull-right button")).click()


class ImportTerminologyPage:
    # ELEMENTS
    # --------
    ICON = (By.CSS_SELECTOR, "a[href='#!/administration']")
    TERMINOLOGY_EDITOR = (By.CSS_SELECTOR, "[ng-if='access.terminology']")
    TERMINOLOGY_NAME = (By.CSS_SELECTOR, "input[name=terminology_name]")
    TERMINOLOGY_RESOURCE = (By.CSS_SELECTOR, "[ng-model='import.terminology.resource_name']")
    HEADER_CHECKBOX = (By.CSS_SELECTOR, "[for='header'] + div")
    LEVEL_IMPORT_1 = (By.CSS_SELECTOR, "[name = 'import_parsing_max_levels']")
    MAP_ICON = (By.CSS_SELECTOR, ".table-header a")
    BUTTON_RUN = (By.CSS_SELECTOR, ".btn-success")

    BUTTON_CANCEL = (By.CSS_SELECTOR, ".content-actionbar a")
    TERMINOLOGY_NAME_DETAIL = (By.CSS_SELECTOR, ".content-header .ng-binding")
    TERMINOLOGY_RESOURCE_NAME_DETAIL = (By.CSS_SELECTOR, "[name='resource_name']")
    SEARCH_TERMINOLOGY_INTERNAL_TEXTBOX = (By.CSS_SELECTOR, ".content-searchbox-input")
    DELETE_ICON = (By.CSS_SELECTOR, ".hover-buttons-td")
    BUTTON_CANCEL_MODEL = (By.CSS_SELECTOR, ".modal-footer .btn-danger")
    LINK_NEW_TER = (By.CSS_SELECTOR, ".list-horizontal a")
    BUTTON_ACTION = (By.CSS_SELECTOR, ".pull-right button")

    # ACTIONS
    # -------
    def enter_name(self, name_terminology):
        logger.info(f"Enter name: {name_terminology}")
        send_keys(self.TERMINOLOGY_NAME, name_terminology, False, True)

    def enter_resource_name(self, resource_terminology):
        logger.info(f"Enter name: {resource_terminology}")
        send_keys(self.TERMINOLOGY_RESOURCE, resource_terminology, False, True)

    def click_on_administrator_icon(self):
        logger.info("1. Go to Administration Page")
        find_element(self.ICON).click()

    def click_on_terminology_editor(self):
        logger.info("2. Go to Terminology Editor.")
        find_element(self.TERMINOLOGY_EDITOR).click()

    def click_on_import_on_dropdown_list(self):
        logger.info("4. Click on the Import on drop down list")
        find_element((By.CSS_SELECTOR, "[href = '#!/terminology/import/0']")).click()

    def select_target_terminology_dropdown(self, value):
        logger.info(f"Select Target terminology: {value}")

    def enter_csv_file(self, csv_file):
        logger.info("5. Upload file ")
        find_element((By.CSS_SELECTOR, "input[type=file]")).send_keys(csv_file)
        pass

    def click_map_icon(self):
        logger.info(". Click on Map icon ")
        find_element(self.MAP_ICON).click()
        pass

    def click_on_run_button(self):
        logger.info(". Click on Run button")
        find_element(self.BUTTON_RUN).click()
        pass

    def click_on_show_terminology(self):
        logger.info(". Click on show Terminology")
        find_element(self.LINK_NEW_TER).click()
        pass

    def click_on_action_button(self):
        logger.info(". Click on action button")
        find_element(self.BUTTON_ACTION).click()
        pass

    def verify_terminology_name(self,name_terminology):
        logger.info(". Verify Terminology Name")
        assert find_element(self.TERMINOLOGY_NAME_DETAIL).text == name_terminology

        pass

    def click_on_cancel_button(self):
        logger.info(". Click on Cancel button to back on Entity list of Terminology")
        find_element(self.BUTTON_CANCEL).click()
        pass
