import platform

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from src.consts import consts


def create_chrome_driver() -> WebDriver:
    try:
        os_name = platform.system()  # Mac: Darwin | Win: Windows | Linux: Linux
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--incognito")
        # if headless:
        #     chrome_options.add_argument("--headless")
        # else:
        #     chrome_options.add_argument("--start-fullscreen")
        # if user_profile:
        #     if os_name == "Windows":
        # Handle Chrome appears quit unexpectedly popup
        # __modify_file_as_text(user_profile + "\\Default\\Preferences", "Crashed", "none")
        # if extension:
        #     chrome_options.add_argument("--load-extension=" + extension)
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "download.default_directory": consts.DOWNLOAD_DIR,
            "download.directory_upgrade": True,
            "download.prompt_for_download": False
        })
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        driver.maximize_window()
        # if headless:
        # Unable to set full screen in headless mode
        # Issue: https://bugs.chromium.org/p/chromium/issues/detail?id=737535
        # driver.set_window_size(1920, 1080)
        return driver
    except Exception as ex:
        raise Exception("Failed to create Chrome browser driver: %s" % ex)


def create_firefox_driver(headless=False):
    options = Options()
    options.headless = headless
    try:
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        driver.maximize_window()
        return driver
    except Exception as ex:
        raise Exception("Failed to create Firefox browser driver: %s" % ex)
