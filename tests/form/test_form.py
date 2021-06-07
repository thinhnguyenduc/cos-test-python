from random import randint

from src.pages.form.form_page import FormPage
from src.utils import logger
from tests.form.base_suite1 import BaseSuite1


class TestCase1(BaseSuite1):

    def test_case_create_a_form(self):
        form = FormPage()
        form.verify_dashboard()
        form.click_on_administrator_icon()

        form.click_on_form_design()
        form.click_on_new_button()
        form.enter_singular_label("")
        form.enter_plural_label("")
        form.enter_resource_name("")

        self.add_textbox(form)
      #  self.add_autoincrement(form)

        logger.info(". Step 1")
        logger.info(". Step 2")
        logger.info(". Step 3")
        logger.info(f"Title: {self.driver.title}")
        assert self.driver.title == "ClickOnSite"

    def add_textbox(self,form: FormPage):
        resource_name = "textbox_" + str(randint(50, 1001))
        form.click_on_new_icon()
        form.select_field_type("Textfield")
        form.enter_label(resource_name)
        form.enter_resource_name_field(resource_name)
        form.select_checkbox_shortlist()
        pass

    def add_autoincrement(self, form: FormPage):
        form.click_on_new_icon()
        form.select_field_type("Textfield")
        pass