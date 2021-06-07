from src.consts import consts
from src.pages.ultilities.backup_restore_page import System_page
from src.utils import file_util
from tests.suite2.base_suite2 import BaseSuite2


class TestCase_12243(BaseSuite2):

    def test_case_restore_backup(self):
        system = System_page()
        system.verify_dashboard()
        file = consts.DOWNLOAD_DIR + "acme_test_ecosystem_configuration.zip"
        system.click_on_administrator_icon()

        system.click_on_ultilities()
        file_util.delete_file(file)
        system.click_on_backup_system()
        system.verify_file_download(file)
        system.click_on_restore_configuration(file)
        file_util.delete_file(file)
        assert True
