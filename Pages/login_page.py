from selenium.webdriver.common.by import By
from Pages.base_page import basepage

class LoginPage(basepage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.NAME, "usernamw")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
    
    def enter_username(self, username):
        self.find(self.username_input).send_keys(username)

    def enter_password(self, password):
        self.find(self.password_input).send_keys(password)

    def click_login(self):
        self.click(self.login_button)
    