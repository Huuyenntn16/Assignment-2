import requests
from selenium.webdriver.common.by import By

from Pages.base_page import basepage

class NewsFeedAPI(basepage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.new_feed_button = (By.CLASS_NAME, "orangehrm-buzz-widget-header")

    def test_api_get_news(self, api):
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.get(api, json={}, headers=headers)

        print("Status code:", response.status_code)
        print("Response text:", response.text)

        assert response.status_code == 200, "News Feed API failed"

    def test_api_like_action(self, api):
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(api, json={}, headers=headers)

        print("Status code:", response.status_code)
        print("Response text:", response.text)

        assert response.status_code == 200, "Like action API failed"

    def click_new_feed_button(self):
        self.find(self.new_feed_button).click()
        print("Clicked on the New Feed button")



