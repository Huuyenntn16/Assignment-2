import pytest
from selenium import webdriver
from Utils.config_reader import ConfigReader

class BaseTest: 
  @pytest.fixture(autouse=True)
  def setup(self):
    config = ConfigReader.get_config()
    BaseTest.driver = webdriver.Chrome()
    BaseTest.driver.get(ConfigReader.get_url())
    BaseTest.driver.maximize_window()
    yield
    BaseTest.driver.quit