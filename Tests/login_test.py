from .base_test import BaseTest
from Pages.login_page import LoginPage
from Utils.config_reader import ConfigReader

import allure
import time

class TestLogin(BaseTest):
    @allure.feature("Login Feature")
    @allure.story("User Login")
    def test_login(self):
        login_page = LoginPage(self.driver)
        config = ConfigReader.load_config()
        
        time.sleep(5)
        self.allure_screenshot("login_success_screenshot")

        login_page.login(config.username, config.password)

        time.sleep(5)
        self.allure_screenshot("dashboard_screenshot")

        self.teardown()
        
        
