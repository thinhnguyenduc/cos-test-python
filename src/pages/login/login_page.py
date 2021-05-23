from selenium.webdriver.common.by import By

from src.utils import logger
from src.utils.element import click, send_keys, wait_for_element_displayed


class LoginPage:
    # Elements
    # --------
    __USER_INPUT = (By.XPATH, "//input[@placeholder='User ID']")
    __PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")
    __SIGN_ME_IN_BUTTON = (By.XPATH, "//button[text()='Sign me in']")

    # Actions
    # -------
    def type_user(self, user):
        wait_for_element_displayed(self.__USER_INPUT)
        send_keys(self.__USER_INPUT, user)
        logger.info(f"Type user id: '{user}'")

    def type_password(self, password):
        send_keys(self.__PASSWORD_INPUT, password)
        logger.info(f"Type password: '{password}'")

    def click_sign_me_in_button(self):
        click(self.__SIGN_ME_IN_BUTTON)
        logger.info("Click 'Sign me in' button")
