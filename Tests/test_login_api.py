
from Api.login_api import LoginAPI
from Tests.base_test import BaseTest
from Utils.config_reader import ConfigReader


class TestAPILogin(BaseTest):
    def test_api_login(self):
        login_api = LoginAPI(self.driver)
        config = ConfigReader.load_config()

        login_api.test_api_login(config.get_login_api(), config.get_username(), config.get_password())

        self.teardown()


