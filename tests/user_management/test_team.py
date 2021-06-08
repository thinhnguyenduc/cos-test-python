import random
import string

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.utils import logger, common
from src.utils.element import find_element, wait_for_element_displayed
from tests.master_test import MasterTest


class TC2966(MasterTest):
    ICON_ADMIN = (By.CSS_SELECTOR, "a[href='#!/administration']")
    ICON_SEARCH = (By.CSS_SELECTOR, "button[name='search']")
    TEAM_ITEM = (By.CSS_SELECTOR, "[href = '#!/entity/team']")
    TEXTBOX_TEAM_NAME = (By.NAME, "team_name")
    BUTTON_SAVE = (By.ID, "btn__entityDetail__save")
    INTERNAL_SEARCH_TEAM = (By.CSS_SELECTOR, "[ng-model='$select.search']")
    DELETE_ICON = (By.CSS_SELECTOR, "button.btn-flat i.fa-remove")
    BUTTON_NEW = (By.ID, "btn__entityList__new")
    BUTTON_CANCEL_MODEL = (By.CSS_SELECTOR, ".modal-content button[ng-click='ok()']")
    BUTTON_CLOSE = (By.ID, "btn__entityDetail__cancel")
    TEXTBOX_SEARCH_INTERNAL = (By.CSS_SELECTOR, "input[type='search']")
    ROW = (By.CSS_SELECTOR, ".hover-actions.ng-scope")
    TEXT_AFTER_DELETING = (By.CSS_SELECTOR, "span translate")
    MESSAGE_TOOLTIP = (By.CSS_SELECTOR, ".message.ng-binding")

    def test_case_user_management_create_new_team(self):
        logger.info("1. Go to Admin Page")
        find_element(self.ICON_ADMIN).click()

        logger.info("2. Click on Team link")
        find_element(self.TEAM_ITEM).click()

        logger.info("3. Click on New button")
        find_element(self.BUTTON_NEW).click()

        logger.info("4. Enter Team Name ")
        letters = string.ascii_lowercase  # define the specific string
        # define the condition for random.sample() method
        result1 = ''.join((random.sample(letters, 3)))
        name_team = result1 + " QC TEAM"
        find_element(self.TEXTBOX_TEAM_NAME).send_keys(name_team)

        logger.debug(name_team)

        logger.info("5. Click Save button")
        find_element(self.BUTTON_SAVE).click()

        logger.info("6. Click on Close button to go to team list")
        find_element(self.BUTTON_CLOSE).click()

        logger.info("7. Enter on internal search")
        element = find_element(self.TEXTBOX_SEARCH_INTERNAL)
        element.send_keys(name_team)

        common.sleep(2)
        logger.info("8. Click on icon Search")
        # move hover the row

        find_element(self.ICON_SEARCH).click()
        common.sleep(2)  # wait to load

        logger.info("9. Delete the team above")
        row = find_element(self.ROW)

        logger.info("9.1 Move over on the row")
        hover = ActionChains(self.driver).move_to_element(row)
        hover.perform()

        find_element(self.DELETE_ICON).click()

        logger.info("10. Display a warning popup and click on Delete button")
        find_element(self.BUTTON_CANCEL_MODEL).click()

        logger.info("11. Verify the message of tool tip after deleting")
        wait_for_element_displayed(self.MESSAGE_TOOLTIP)
        message_tooltip = find_element(self.MESSAGE_TOOLTIP).text
        assert message_tooltip == "Record has been deleted."
        logger.debug({message_tooltip})

        logger.info("12. Verify the message displays on the list entity")
        element_text = find_element(self.TEXT_AFTER_DELETING).text
        logger.debug({element_text})
        assert element_text == "no data to display"

        common.sleep(2)
#
