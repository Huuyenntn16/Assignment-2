from .base_test import BaseTest
from Pages.login_page import LoginPage
from Utils.config_reader import ConfigReader
import allure

class TestLogin(BaseTest):
    @allure.story("valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_valid(self):
        login_page = LoginPage(self.driver)
        login_page.dologin(ConfigReader.get_username(), ConfigReader.get_password())