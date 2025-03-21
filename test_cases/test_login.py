import pytest

from page_objects.loginpage import LoginPage
from utilities.config_reader import ConfigReader

@pytest.mark.usefixtures("init_driver")
class TestLogin:

    @pytest.fixture(autouse=True)
    def setup_objects(self):
        self.reader=ConfigReader()
        self.login_page=LoginPage(self.driver)
        self.url=self.reader.get_base_url()



    def test_login_with_valid_creds(self):
        login_creds = self.reader.get_login_creds()
        self.login_page.open_url(self.url)
        self.login_page.login_user(login_creds[0], login_creds[1])

    def test_login_with_invalid_creds(self):
        self.login_page.open_url(self.url)
        self.login_page.login_user("invalid", "password")