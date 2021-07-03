from random import randint

import allure

from src.pages.form.form_page import FormPage
from src.utils import common, logger
from tests.form import BaseTestForm


class TCNewForm(BaseTestForm):

    @allure.title("Create a new form")
    def test(self):
        try:
            # Start test
            form = FormPage()
            self.go_to_formbuilder(form)
            form_name = "form" + str(randint(50, 1001))
            resource_name = "textbox_" + str(randint(50, 1001))
            self.fill_data_form(form_name, form)
            self.add_texfield(resource_name, form)
            form.click_save_button()
            common.sleep(2)
            self.add_autoincrement(form)
            common.sleep(2)
            form.click_save_button()
            form.click_on_icon_go_to_entity_list()
            self.add_new_entity(resource_name, form)
            self.delete_form(form_name, form)
            # End test
        except Exception as ex:
            logger.error(ex)
            self.failures.append(ex)
        finally:
            self.screenshot_binary_data.append(self.save_screenshot())

    def go_to_formbuilder(self, form: FormPage):
        common.sleep(5)
        form.click_on_administrator_icon()
        common.sleep(2)
        form.click_on_form_design()
        form.click_on_new_button_form_list()

    def fill_data_form(self, form_name, form: FormPage):
        form.enter_singular_label(form_name)
        form.enter_plural_label(form_name)
        form.enter_resource_name(form_name)

    def add_texfield(self, resource_name, form: FormPage):
        form.click_on_new_icon()
        form.select_field_type("Textfield")
        form.enter_label(resource_name)
        common.sleep(5)
        form.click_on_checkbox("Short lists")
        common.sleep(5)

    def add_new_entity(self, resource_name, form: FormPage):
        form.click_on_new_button_entity_list()
        form.enter_data_on_textbox(resource_name, "hi")
        form.click_save_button_on_entity_detail()
        common.sleep(5)

    def add_autoincrement(self, form: FormPage):
        form.click_on_new_icon()
        form.select_field_type("Autoincrement")
        form.enter_title("ID Product")
        form.click_on_checkbox("string")
        common.sleep(2)
        form.click_on_checkbox("prefix")
        form.enter_prefix("MA")
        common.sleep(5)

    def delete_form(self, form_name, form: FormPage):
        common.sleep(2)
        form.click_on_administrator_icon()
        common.sleep(2)
        form.click_on_form_design()
        common.sleep(1)
        form.enter_form_name_on_internal_search(form_name)
        common.sleep(1)
        form.move_hover_on_row()
        assert form.get_title_form_after_searching() == form_name
        form.click_on_delete_icon()
        form.click_delete_button()
