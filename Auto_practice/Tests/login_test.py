from Pages.base_page import BaseTest
from Pages.login_page import LoginPage

class TestLoginWeb(BaseTest):
    def test_login_valid(self):
        login_page = LoginPage(self.driver)
        login_page.dologin()
        
