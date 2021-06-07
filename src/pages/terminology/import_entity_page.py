from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.utils import logger
from src.utils.element import find_element, send_keys, send_keys_chord


class Import_entity_page:
    ICON_ADMIN = (By.CSS_SELECTOR, "a[href='#!/administration']")
    LINK_FORM_DESIGNER = (By.CSS_SELECTOR, "[ng-if='access.formbuilder']")
    TEXTBOX_SEARCH = (By.CSS_SELECTOR, "[ng-model='screen.helper.search']")
    LINK_ROW_SEARCH_RESULT = (By.CSS_SELECTOR, "[href='#!formbuilder/edit/177']")
    ICON_HUMBERGER = (By.ID, "btn__formbuilder__designer__entityList")
    BUTTON_NEW = (By.CSS_SELECTOR, ".btn-primary .fa.fa-plus")
    ITEM_ENTITY = (By.ID, "btn__entityList__new__import__entity")
    SELECT_TARGET_ENTITY = (By.ID, "targetEntity")
    SELECT_OPERATION = (By.ID, "importOperation")
    TEXTBOX_FILE = (By.ID, "sourceFile")
    MAP_ICON = (By.CSS_SELECTOR, ".table-header a")
    MAP_PREFIX = (By.XPATH, "//td[@class='ng-binding' and text()='WO - ID - prefix']/following-sibling::td[1]/a")
    MAP_NUMBER = (By.XPATH, "//td[@class='ng-binding' and text()='WO - ID - number']/following-sibling::td[1]/a")
    TEXTBOX_SEARCH_ON_POPUP = (By.CSS_SELECTOR, "[ng-if='dropdownNodes'] .selectize-input .ui-select-search")

    MAP_PREFIX_ON_POPUP = (
        By.XPATH, "//*[text()='Site takes place on Work order']/../following-sibling::treeitem/ul/li/div")
    LINK_ITEM_AUTO_COMPLETE_ON_POPUP = (By.CSS_SELECTOR, ".ui-select-choices-row-inner span")
    # [ng - click = 'ok()']
    BUTTON_OK_ON_POPUP = (By.CSS_SELECTOR, ".[ng-click ='ok()']")

    def click_on_icon_admin(self):
        logger.info(". Go to Administration Page")
        find_element(self.ICON_ADMIN).click()
        pass

    def click_on_form_designer_link(self):
        logger.info(". Click on Design link")
        find_element(self.LINK_FORM_DESIGNER).click()
        pass

    def enter_textbox_search(self, value):
        logger.info(f"Enter textbox search on form: {value}")
        send_keys(self.TEXTBOX_SEARCH, value, True, False)
        pass

    def click_on_report_form(self):
        logger.info(f" Click on Import form")
        find_element(self.LINK_FORM_IMPORT).click()
        pass

    def click_on_row_on_search_result(self):
        logger.info(f" Click on Import form")
        find_element(self.LINK_ROW_SEARCH_RESULT).click()
        pass

    def click_on_icon_humberger(self):
        logger.info(f" Click on icon Humberger to go to entity list")
        find_element(self.ICON_HUMBERGER).click()
        pass

    def click_on_button_new(self):
        logger.info(f" Click on  New button")
        find_element(self.BUTTON_NEW, timeout=90).click()
        pass

    def clicK_on_entity_on_dropdown_list(self):
        logger.info(f" Click on item entity to go to import for entity")
        find_element(self.ITEM_ENTITY, timeout=90).click()
        pass

    def select_on_target_entity_dropdownlist(self, param):
        logger.info(f" Select Site : {param}")
        element = find_element(self.SELECT_TARGET_ENTITY, timeout=90)
        select = Select(element)
        select.select_by_visible_text(param)
        pass

    def select_file_csv(self, csv_file):
        logger.info(". Upload file ")
        find_element((By.CSS_SELECTOR, "input[type=file]")).send_keys(csv_file)
        pass

    def select_operation(self, param):
        logger.info(f" Select Site : {param}")
        select = Select(find_element(self.SELECT_OPERATION))
        select.select_by_visible_text(param)
        pass

    def click_on_map_prefix_icon(self):
        logger.info(". Click on Map Prefix icon ")
        find_element(self.MAP_PREFIX).click()

    def enter_prefix_on_search(self, param):
        logger.info(f". Click on prefix  {param}")
        send_keys_chord(self.TEXTBOX_SEARCH_ON_POPUP, param, True, True)

    def click_on_map_prefix(self):
        logger.info(f". Click on Map Prefix icon ")
        find_element(self.MAP_PREFIX_ON_POPUP).click()

    def click_on_item_on_autocomplete(self):
        logger.info(f". Click on item on auto complete ")
        find_element(self.LINK_ITEM_AUTO_COMPLETE_ON_POPUP).click()
        pass

    def click_on_ok_button_on_popup(self):
        logger.info(f". Click on button OK on popup ")
        find_element(self.BUTTON_OK_ON_POPUP).click()
        pass

    def click_on_map_id(self):
        logger.info(f". Click on link Map Number icon ")
        find_element(self.MAP_NUMBER).click()
        pass

    def click_on_map_icon(self):
        pass
