from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.utils import logger, string_util
from src.utils.element import find_element, send_keys, wait_for_element_displayed, wait_element_invisible


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
        logger.info(f" Enter to singular label")
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

    def select_field_type(self, param):
        logger.info(f" Select Field Type{param}  ")
        element = find_element(self.SELECT_FIELD_TYPE)
        select = Select(element)
        select.select_by_visible_text(param)
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
        #  wait_for_element_displayed(self.ICON_PLUS_FIELD)
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

