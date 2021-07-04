from src.consts import consts
from src.pages.ultilities.backup_restore_page import System_page
from src.utils import file_util
from tests.form import BaseTestForm


class TestCase_12243(BaseTestForm):

    def test_case_restore_backup(self):
        system = System_page()
        system.verify_dashboard()
        file = consts.DOWNLOAD_DIR + "acme_test_ecosystem_configuration.zip"
        system.click_on_administrator_icon()
        system.click_on_ultilities()
        file_util.delete_file(file)
        system.click_on_backup_system()
        assert system.verify_file_download(file)
        system.click_on_restore_configuration(file)
        # assert system.verify_file_download(file)  # verify text 'Finished' displayed
        file_util.delete_file(file)
