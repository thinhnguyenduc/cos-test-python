from selenium.webdriver.common.by import By

from src.utils import logger
from src.utils.element import find_element


class FormPage:
    LINK_FORM = (By.CSS_SELECTOR, "a[href = '#!/formbuilder")
    ICON_ADMIN = (By.CSS_SELECTOR, "a[href='#!/administration']")
    BUTTON_NEW = (By.CSS_SELECTOR, ".btn__formbuilder__addNewEntity")
    TEXTBOX_SINGULAR_LABEL = (By.ID, "formSingularLabel")
    TEXTBOX_PLURAL_LABLE = (By.ID, "formPluralLabel")
    TEXTBOX_RESOURCE_NAME = (By.ID, "formType")
    ICON_PLUS_FIELD = (By.ID, "[data-toogle='tab']  i.fa-plus")
    SELECT_FIELD_TYPE = (By.ID, "fieldType")
    TEXTBOX_TITLE = (By.ID, "fieldTitle")
    #systemName
    TEXTBOX_SYSTEM_NAME = (By.ID, "systemName")
    DASHBOARD = (By.CSS_SELECTOR, ".sidebar-menu a[href='#!/dashboard'] span")  # .sidebar-menu a[href='#!/dashboard']

    #
    def click_on_administrator_icon(self):
        logger.info(f"Click on Admin icon :")
        find_element(self.ICON_ADMIN, timeout=90).click()
        pass

    pass

    def click_on_form_design(self):
        logger.info(f"Click on Form design on admin page :")
        find_element(self.LINK_FORM).click()
        pass

    def verify_dashboard(self):
        logger.info(f"Verify dashboad ")
        header_text = find_element(self.DASHBOARD, timeout=60).text
        logger.info(f"Verify header = {header_text} ")
        assert header_text == "Dashboard"
        pass

    def click_on_new_button(self):
        logger.info(f"Click on New button")
        find_element(self.BUTTON_NEW).click()
        pass

    def enter_singular_label(self, param):
        pass

    def enter_plural_label(self, param):
        pass

    def enter_resource_name(self, param):
        pass

    def select_field_type(self, param):
        pass

    def enter_label(self):
        pass

    def enter_resource_name_field(self, param):
        pass

    def select_checkbox_shortlist(self):
        pass

    def click_on_new_icon(self):
        pass
