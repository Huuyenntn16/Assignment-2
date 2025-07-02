from pages.base_login_page import BaseLoginPage

class LoginPage(BaseLoginPage):
    def __init__(self, driver):
        super().__init__(driver)
        
def login(self, username="Admin", password="admin123"):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
   
