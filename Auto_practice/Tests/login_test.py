from Pages.base_page import BaseTest
from Pages.login_page import LoginPage

class TestLogin(BaseTest):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login()
        
