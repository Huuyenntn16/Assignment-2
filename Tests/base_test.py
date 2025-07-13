import pytest
from selenium import webdriver
from Utils.config_reader import ConfigReader

class BaseTest: 
  @pytest.fixture(autouse=True)
  def setup(self):
      
    config = ConfigReader.load_config()

    BaseTest.driver = webdriver.Chrome()
    BaseTest.driver.get(config.base_url)
    BaseTest.driver.maximize_window()


  def teardown(self):
    self.driver.quit()