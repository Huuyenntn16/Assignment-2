from selenium.webdriver.common.by import By
from Pages.base_page import basepage
from selenium.webdriver.support import expected_conditions as EC
import allure

class LoginPage(basepage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

   
    def login(self, username, password):
        self.find(self.username_input).send_keys(username)
        self.find(self.password_input).send_keys(password)
        self.click(self.login_button)


    def allure_screenshot(self, name="dashboard_screenshot"):
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
        with open("Report/{}.png".format(name), "wb") as f:
            f.write(screenshot)
    