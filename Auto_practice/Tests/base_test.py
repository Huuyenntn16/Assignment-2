import pytest
from selenium import webdriver

class Basetest: 
  @pytest.fixture
  def setup(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.get("https://opensource-demo.orangehrmlive.com/")
    yield
    self.driver.quit()
