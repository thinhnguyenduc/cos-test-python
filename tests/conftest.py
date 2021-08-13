import builtins

import pytest

from src.consts import consts
from src.pages.login.login_page import LoginPage
from src.utils import logger, file_util
from src.utils.browser_driver import create_chrome_driver


def pytest_addoption(parser):
    parser.addoption("--env", action="store")


@pytest.fixture(scope="session", autouse=True)
def session_start(request):  # Before all tests, run this function one time only.
    logger.info("=== Start Pytest session ===")

    # Read environment from a parameter named 'env'
    env = request.config.getoption("--env")
    config = file_util.read_properties_file(consts.ENV_CONFIG_FILE.format(env))
    file_util.create_folder(consts.SCREENSHOT_DIR.format(env))
    consts.ENV_CONFIG_FILE.format(env)

    # Init Chrome driver
    driver = create_chrome_driver()
    builtins.driver = driver
    builtins.env = env
    builtins.url = config["url"]

    # Navigate to test site
    driver.get(config["url"])
    login_page = LoginPage()
    login_page.type_user(config["username"])
    login_page.type_password(config["password"])
    login_page.click_sign_me_in_button()


def pytest_sessionfinish(session):
    # Quit Chrome driver
    if hasattr(builtins, "driver"):
        getattr(builtins, "driver").quit()
    logger.info("=== End Pytest session ===")
