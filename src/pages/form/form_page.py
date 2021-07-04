import builtins

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.utils import logger, string_util
from src.utils.element import find_element, send_keys, wait_for_element_displayed, wait_element_invisible, \
    move_hover_element, wait_for_elements_displayed


class FormPage:
    LINK_FORM = (By.CSS_SELECTOR, "a[href = '#!/formbuilder")
    ICON_ADMIN = (By.CSS_SELECTOR, "a[href='#!/administration']")
    BUTTON_NEW = (By.CSS_SELECTOR, ".btn__formbuilder__addNewEntity")
    TEXTBOX_SINGULAR_LABEL = (By.ID, "formSingularLabel")
    TEXTBOX_PLURAL_LABEl = (By.ID, "formPluralLabel")
    TEXTBOX_RESOURCE_NAME = (By.ID, "formType")
    ICON_PLUS_FIELD = (By.CSS_SELECTOR, "[ng-click='tab.action()']")
    SELECT_FIELD_TYPE = (By.ID, "fieldType")
    TEXTBOX_TITLE = (By.CSS_SELECTOR, "input#fieldTitle")
    CHECKBOX_SHORTLIST = (By.XPATH, "//input[@type='checkbox'][@ng-model='field.show_in_lists_short']/..")
    # input#fieldTitle

    TEXTBOX_SYSTEM_NAME = (By.CSS_SELECTOR, "input#systemName")
    DASHBOARD = (By.CSS_SELECTOR, ".sidebar-menu a[href='#!/dashboard'] span")  # .sidebar-menu a[href='#!/dashboard']
    BUTTON_SAVE = (By.CSS_SELECTOR, ".btn__formbuilder__saveForm")
    ICON_ENTITY_LIST = (By.CSS_SELECTOR, "[title='Go to entity list']")
    MESSAGE_SUCCESSFUL = (By.CSS_SELECTOR, '.success')
    PROGRESS_BAR = (By.CSS_SELECTOR, ".progress-bar")
    BUTTON_NEW_ENTITY = (By.CSS_SELECTOR, "[ng-click='go(newEntryUrl, {})']")
    BUTTON_SAVE_ENTITY_DETAIL = (By.XPATH, "//*[text()='Save']")
    __TEXTBOX_NAME = (By.CSS_SELECTOR, "[name='%s']")
    CHECKBOX_FORM_SETTING = (By.XPATH, "//*[text()='%s']/../div")
    # Form  design
    TEXTBOX_INTERNAL_SEARCH_FORM = (By.CSS_SELECTOR, "[ng-model='screen.helper.search']")
    ROW_SEARCH_RESULT = (By.CSS_SELECTOR, "tr.hover-actions")
    ICON_DELETE_FORM = (By.CSS_SELECTOR, "button.btn-mini")
    TITLE_FORM = (By.CSS_SELECTOR, "tr a")
    BUTTON_DELETE_ON_POPUP = (By.CSS_SELECTOR, "[ng-click='ok()']")

    # Dropdown list
    BUTTON_ADD_OPTION = (By.CSS_SELECTOR, "[ng-click='addOption(field)']")
    TEXTBOX_OPTION = (By.XPATH, "//*[text()='%s']/../input")
    TEXTBOX_LABEL_DDL = (By.ID, "fieldTitle")
    TEXTBOX_PREFIX = (By.ID, "fieldStringPrefix")
    # Relation popup
    SELECT_SOURCE_FORM = (By.CSS_SELECTOR, "[name='source_id']")
    SELECT_TARGET_FORM = (By.CSS_SELECTOR, "[name='target_id']")
    TEXTBOX_RESOURCE_RELATION = (By.NAME, "system_name")
    TEXTBOX_MIN = (By.NAME, "min")
    TEXTBOX_MAX = (By.NAME, "max")
    BUTTON_SAVE_RELATION_POPUP = (By.CSS_SELECTOR, "[ng-click='ok()']")

    # Authority
    TEXTBOX_AUTHORITY = (By.CSS_SELECTOR, "[ng-model='field.authorities']")
    OPTIONS_AUTHORITY = (By.CSS_SELECTOR, ".ui-select-choices-row-inner div")
    OPTION_AUTHORITY = (By.XPATH, "//*[contains(text(),'%s')]")
    TEXTBOX_ENTITY_AUTHORITY = (By.CSS_SELECTOR, "label[for='%s']+div")

    def click_on_administrator_icon(self):
        logger.info(f"Click on Admin icon :")
        wait_for_element_displayed(self.ICON_ADMIN)
        find_element(self.ICON_ADMIN, timeout=90).click()

    def click_on_form_design(self):
        logger.info(f"Click on Form design on admin page :")
        find_element(self.LINK_FORM).click()
        pass

    def verify_dashboard(self):
        logger.info(f"Verify dashboad ")
        header_text = find_element(self.DASHBOARD, timeout=60).text
        logger.info(f"Verify header = {header_text} ")
        assert header_text == "Dashboard"

    def click_on_new_button_form_list(self):
        logger.info(f"Click on New button")
        wait_for_element_displayed(self.BUTTON_NEW)
        find_element(self.BUTTON_NEW).click()

    def enter_singular_label(self, param):
        logger.info(f" Enter to singular label +{param}")
        wait_for_element_displayed(self.TEXTBOX_SINGULAR_LABEL)
        send_keys(self.TEXTBOX_SINGULAR_LABEL, param)
        pass

    def enter_plural_label(self, param):
        logger.info(f" Enter to plural label")
        wait_for_element_displayed(self.TEXTBOX_PLURAL_LABEl)
        send_keys(self.TEXTBOX_PLURAL_LABEl, param)
        pass

    def enter_resource_name(self, param):
        logger.info(f" Enter resource name")
        wait_for_element_displayed(self.TEXTBOX_RESOURCE_NAME)
        send_keys(self.TEXTBOX_RESOURCE_NAME, param)
        pass

    def select_field_type(self, option_value, resource_name=SELECT_FIELD_TYPE):
        logger.info(f" Select Field Type of {resource_name}")
        logger.debug(resource_name)
        element = find_element(self.SELECT_FIELD_TYPE)
        select = Select(element)
        select.select_by_visible_text(option_value)

    pass

    def select_field_type2(self, option_value, resource_name):
        logger.info(f" Select Field Type of {resource_name}")
        logger.debug(resource_name)
        new_locator = (By.ID, resource_name)
        element = find_element(new_locator)
        select = Select(element)
        select.select_by_visible_text(option_value)

    pass

    def enter_label(self, param):
        logger.info(f" Enter label{param}  ")
        wait_for_element_displayed(self.TEXTBOX_TITLE)
        send_keys(self.TEXTBOX_TITLE, param)
        pass

    def enter_resource_name_field(self, param):
        logger.info(f" Enter resource name {param}")
        send_keys(self.TEXTBOX_SYSTEM_NAME, param)
        pass

    def click_on_checkbox_shortlist(self):
        logger.info(f" Click on Check box Short List ")
        result = wait_for_element_displayed(self.CHECKBOX_SHORTLIST)
        logger.debug(f"result{result}")
        element = find_element(self.CHECKBOX_SHORTLIST)
        element.click()
        pass

    def click_on_new_icon(self):
        logger.info(f" Click on icon + to add field  ")
        find_element(self.ICON_PLUS_FIELD).click()
        pass

    def click_save_button(self):
        logger.info(f" Click on Save button ")
        find_element(self.BUTTON_SAVE).click()

    def click_on_icon_go_to_entity_list(self):
        logger.info(f" Go to entity list")
        wait_for_element_displayed(self.ICON_ENTITY_LIST)
        find_element(self.ICON_ENTITY_LIST).click()

    def get_message_successful(self) -> str:
        logger.info(f" Wait for progress bar invissible")
        wait_element_invisible(self.PROGRESS_BAR)
        logger.info(f" Wait for tooltip appear")
        wait_for_element_displayed(self.MESSAGE_SUCCESSFUL)
        element = find_element(self.MESSAGE_SUCCESSFUL)
        assert element.text == "Form has been saved."
        logger.info(f" Verify message :{element.text}")
        return find_element(self.MESSAGE_SUCCESSFUL).text

    def get_message_save_entity_successful(self) -> str:
        logger.info(f" Wait for progress bar invissible")
        wait_element_invisible(self.PROGRESS_BAR)
        logger.info(f" Wait for tooltip appear")
        wait_for_element_displayed(self.MESSAGE_SUCCESSFUL)
        element = find_element(self.MESSAGE_SUCCESSFUL)

        logger.info(f" Verify message :{element.text}")
        return find_element(self.MESSAGE_SUCCESSFUL).text

    def click_on_new_button_entity_list(self):  # param = abc
        logger.info(f" Click on button add new entity")
        find_element(self.BUTTON_NEW_ENTITY).click()

    def enter_data_on_textbox(self, param, value):
        logger.info(f" enter new entity")
        new_xpath = string_util.cook_element(self.__TEXTBOX_NAME, param)
        send_keys(new_xpath, value)

    def click_save_button_on_entity_detail(self):
        logger.info(f" Click on Save button")
        find_element(self.BUTTON_SAVE_ENTITY_DETAIL).click()

    def click_on_checkbox(self, param):
        new_xpath = string_util.cook_element(self.CHECKBOX_FORM_SETTING, param)
        element = find_element(new_xpath)
        driver = getattr(builtins, "driver")
        driver.execute_script("window.scrollTo(0, 0);")
        action = ActionChains(driver)
        action.move_to_element(element).click().perform()
        pass

    def enter_form_name_on_internal_search(self, param):
        logger.info(f" Enter form name {param} on internal search")
        wait_for_element_displayed(self.TEXTBOX_INTERNAL_SEARCH_FORM)
        send_keys(self.TEXTBOX_INTERNAL_SEARCH_FORM, param, press_enter=True, clear=True)
        pass

    def move_hover_on_search_result(self, param):
        logger.info(f" Move over on the search result")
        new_xpath = string_util.cook_element(self.ROW_SEARCH_RESULT, param)
        move_hover_element(new_xpath)
        pass

    def click_on_delete_icon(self):
        logger.info(f" Click on Delete icon")
        # wait_for_element_displayed(self.ICON_DELETE_FORM)
        driver = getattr(builtins, "driver")
        # element_to_hover_over = find_element(self.ROW_SEARCH_RESULT)
        # hover = ActionChains(driver).move_to_element(element_to_hover_over)
        # hover.perform()
        find_element(self.ICON_DELETE_FORM).click()
        pass

    def get_title_form_after_searching(self):
        wait_for_element_displayed(self.TITLE_FORM)
        return find_element(self.TITLE_FORM).text

    def click_delete_button(self):
        logger.info(f" Click on Delete icon on Popup ")
        find_element(self.BUTTON_DELETE_ON_POPUP).click()
        pass

    def move_hover_on_row(self):
        logger.info(f"Move over on search result")
        driver = getattr(builtins, "driver")
        element_to_hover_over = find_element(self.ROW_SEARCH_RESULT)
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()

    # move_hover_element(self.ROW_SEARCH_RESULT)
    pass

    def enter_title(self, param):
        logger.info(f" Enter Title")
        send_keys(self.TEXTBOX_TITLE, param, press_enter=True, clear=True)
        pass

    def enter_prefix(self, param):
        logger.info(f" Enter Prefix")
        send_keys(self.TEXTBOX_PREFIX, param, press_enter=True, clear=True)
        pass

    def select_source_form(self, param):
        element = find_element(self.SELECT_SOURCE_FORM)
        select = Select(element)
        select.select_by_visible_text(param)
        pass

    def select_target_form(self, param):
        element = find_element(self.SELECT_TARGET_FORM)
        select = Select(element)
        select.select_by_visible_text(param)
        pass

    def enter_min(self, param):
        send_keys(self.TEXTBOX_MIN, param, True, True)
        pass

    def enter_max(self, param):
        send_keys(self.TEXTBOX_MAX, param, True, True)
        pass

    def click_save_button_relation_popup(self, param):
        send_keys(self.TEXTBOX_RESOURCE_RELATION, param, True, True)
        pass

    def enter_resource_name_relation_popup(self, param):
        send_keys(self.TEXTBOX_RESOURCE_RELATION, param, True, True)
        pass

    def click_on_add_option_button(self):
        logger.info(f" Click on button Add Option of Dropdown list")
        find_element(self.BUTTON_ADD_OPTION).click()
        pass

    def enter_option(self, param, value):
        logger.info(f" Enter Add Option of Dropdown list")
        new_xpath = string_util.cook_element(self.TEXTBOX_OPTION, param)
        send_keys(new_xpath, value, True, True)

    def enter_title_dropdown_list(self, param):
        logger.info(f" Enter title of dropdown list")
        send_keys(self.TEXTBOX_LABEL_DDL, param, True, True)
        pass

    def fill_authority(self, param):
        logger.info(f" Click on Authority")
        find_element(self.TEXTBOX_AUTHORITY).click()
        logger.info(f" Click on item {param}")
        wait_for_elements_displayed(self.OPTIONS_AUTHORITY)
        new_xpath = string_util.cook_element(self.OPTION_AUTHORITY, param)
        find_element(new_xpath).click()
        pass

    def fill_autocomplete(self, resource_name, option_value):
        new_xpath = string_util.cook_element(self.TEXTBOX_ENTITY_AUTHORITY, resource_name)
        find_element(self.TEXTBOX_ENTITY_AUTHORITY).click()
        wait_for_elements_displayed(self.OPTIONS_AUTHORITY)
        new_xpath = string_util.cook_element(self.OPTION_AUTHORITY, option_value)
        find_element(new_xpath).click()
