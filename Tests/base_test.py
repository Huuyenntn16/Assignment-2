import allure
import pytest
from selenium import webdriver
from Utils.config_reader import ConfigReader

class BaseTest: 
  @pytest.fixture(autouse=True)
  def setup(self):
      
    config = ConfigReader.load_config()

    BaseTest.driver = webdriver.Chrome()
    BaseTest.driver.get(config.base_url)
    # BaseTest.driver.maximize_window()


  def teardown(self):
    self.driver.quit()

  def allure_screenshot(self, name="dashboard_screenshot"):
      screenshot = self.driver.get_screenshot_as_png()
      allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
      with open("Report/{}.png".format(name), "wb") as f:
          f.write(screenshot)