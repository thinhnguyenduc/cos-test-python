from random import randint

import allure

from src.pages.form.form_page import FormPage
from src.utils import common, logger
from tests.form import BaseTestForm


class TCNewForm(BaseTestForm):

    # @allure.title("Create a new form")
    def test_01(self):
        try:
            # Start test
            form = FormPage()
            self.go_to_formbuilder(form)
            form_name = "form" + str(randint(50, 1001))
            resource_name = "textbox_" + str(randint(50, 1001))
            self.fill_data_form(form_name, form)
            self.add_dropdown_list(form)
            form.click_save_button()
            self.add_texfield(resource_name, form)
            form.click_save_button()
            common.sleep(1)
            self.add_autoincrement(form)
            form.click_save_button()
            common.sleep(1)
            form.click_on_icon_go_to_entity_list()

            self.add_new_entity(resource_name, form)
            self.add_entity_for_dropdownlist("1", "dropdown_list", form)
            common.sleep(2)
            form.click_save_button_on_entity_detail()
            messsage = form.get_message_save_entity_successful()
            result= messsage.find("saved")
            assert messsage.find("saved") != 1

            common.sleep(2)
            self.delete_form(form_name, form)
            # End test
        except Exception as ex:
            logger.error(ex)
            self.failures.append(ex)
        finally:
            self.screenshot_binary_data.append(self.save_screenshot())

    @allure.title("Create a new form with duplicate resource")
    def _test_02(self):
        try:
            # Start test
            form = FormPage()
            self.go_to_formbuilder(form)
            assert 1 == 2
            form_name = ""
            resource_name = ""
            self.fill_data_form(form_name, form)
            self.add_texfield(resource_name, form)
            form.click_save_button()

            # End test
        except Exception as ex:
            logger.error(ex)
            self.failures.append(ex)
        finally:
            self.screenshot_binary_data.append(self.save_screenshot())

    def go_to_formbuilder(self, form: FormPage):
        common.sleep(1)
        form.click_on_administrator_icon()
        common.sleep(1)
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
        common.sleep(1)
        form.click_on_checkbox("Short lists")
        common.sleep(1)

    def add_new_entity(self, resource_name, form: FormPage):
        form.click_on_new_button_entity_list()
        form.enter_data_on_textbox(resource_name, "hi")


    def add_autoincrement(self, form: FormPage):
        form.click_on_new_icon()
        form.select_field_type("Autoincrement")
        form.enter_title("ID Product")
        form.click_on_checkbox("string")
        common.sleep(2)
        form.click_on_checkbox("prefix")
        form.enter_prefix("MA")
        common.sleep(5)

    def add_dropdown_list(self, form: FormPage):
        form.click_on_new_icon()
        form.select_field_type("Dropdown list")
        form.enter_title_dropdown_list("dropdown_list")
        form.click_on_add_option_button()
        form.enter_option("1", "1")

    def add_entity_for_dropdownlist(self, opt_value, dropdown_list_resourse, form: FormPage):
        form.select_field_type2(opt_value, dropdown_list_resourse)

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
