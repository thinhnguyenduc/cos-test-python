import builtins

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.utils import logger, file_util
from src.utils.element import find_element, wait_element_invisible, send_keys


class System_page:
    LINK_ULTILITES = (By.CSS_SELECTOR, "a[href = '#!/administration/utilities']")
    ICON_ADMIN = (By.CSS_SELECTOR, "a[href='#!/administration']")
    BUTTON_BACK_UP = (By.CSS_SELECTOR, "[ng-click='exportTenantConfiguration();']")
    PROGRESS_BAR = (By.CSS_SELECTOR, ".progress-bar")
    BUTTON_RESTORE = (By.CSS_SELECTOR, "[ng-click='importTenantConfiguration();']")
    INPUT_FILE = (By.CSS_SELECTOR, "input[type='file']")
    MESSAGE_SUSSCESSFUL = (By.CSS_SELECTOR, ".callout-success h4")
    PROGRESS_UPLOAD_CONFIGURATION = (By.CSS_SELECTOR, ".callout-info")

    HEADER_ADMIN_PAGE = (By.CSS_SELECTOR, ".content-header h1")
    DASHBOARD = (By.CSS_SELECTOR, ".sidebar-menu a[href='#!/dashboard'] span")  # .sidebar-menu a[href='#!/dashboard']

    def click_on_administrator_icon(self):
        logger.info(f"Click on Admin icon :")
        find_element(self.ICON_ADMIN, timeout=90).click()
        pass

    def click_on_ultilities(self):
        logger.info(f"Click on ultilites link: ")
        find_element(self.LINK_ULTILITES, timeout=90).click()
        pass

    def click_on_backup_system(self):
        logger.info(f"Click on Backup button ")
        driver = getattr(builtins, "driver")
        logger.info(f"Move to Back Up button ")
        element = find_element(self.BUTTON_BACK_UP, timeout=60)
        driver.execute_script("window.scrollTo(0, 0);")
        action = ActionChains(driver)
        action.move_to_element(element).click().perform()
        # element.click()
        wait_element_invisible(self.PROGRESS_BAR, timeout=100)
        driver.implicitly_wait(15)
        pass

    def click_on_restore_configuration(self, file):
        logger.info(f"Restore on Backup button ")
        find_element(self.BUTTON_RESTORE, timeout=90).click()
        send_keys(self.INPUT_FILE, file)
        logger.info(f" Wait for upload {file} ")
        wait_element_invisible(self.PROGRESS_UPLOAD_CONFIGURATION, timeout=200)
        self.verify_file_download(file)
        pass

    def verify_message_successful(self):
        logger.info(f"Verify message upload configuration ")
        message = find_element(self.MESSAGE_SUSSCESSFUL, timeout=100).text
        assert message == "Finished"
        logger.info(f"{message}")
        pass

    def verify_header_admin_page(self):
        logger.info(f"Verify header = Administration ")
        header_text = find_element(self.HEADER_ADMIN_PAGE, timeout=60).text
        logger.info(f"Verify header = {header_text} ")
        assert header_text == "Administration"
        pass

    def verify_dashboard(self):
        logger.info(f"Verify dashboad ")
        header_text = find_element(self.DASHBOARD, timeout=60).text
        logger.info(f"Verify header = {header_text} ")
        assert header_text == "Dashboard"
        pass

    def verify_file_download(self, file):
        logger.info(f"Verify {file} is download ")
        return file_util.is_file_exist_in_time(file, 160)
