from random import randint

from src.pages.form.form_page import FormPage
from src.utils import common
from tests.master_test import MasterTest


class TestCase1(MasterTest):

    def test_case_create_a_form(self):
        form = FormPage()
        common.sleep(5)
        form.click_on_administrator_icon()
        common.sleep(2)
        form.click_on_form_design()
        form.click_on_new_button_form_list()
        form_name = "form" + str(randint(50, 1001))
        resource_name = "textbox_" + str(randint(50, 1001))
        form.enter_singular_label(form_name)
        form.enter_plural_label(form_name)
        form.enter_resource_name(form_name)
        self.add_texfield(resource_name, form)
        form.click_on_icon_go_to_entity_list()
        self.add_new_entity(resource_name,form)
        common.sleep(5)

    def add_texfield(self, resource_name, form: FormPage):
        form.click_on_new_icon()
        form.select_field_type("Textfield")
        form.enter_label(resource_name)
        form.click_on_checkbox_shortlist()  # here
        form.click_save_button()
        common.sleep(5)

    def add_new_entity(self, resource_name, form: FormPage):
        form.click_on_new_button_entity_list()
        form.enter_data_on_textbox(resource_name, "hi")
        form.click_save_button_on_entity_detail()
        common.sleep(5)

    def add_autoincrement(self, form: FormPage):
        # form.click_on_new_icon()
        form.select_field_type("Textfield")
