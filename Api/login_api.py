import requests

from Pages.base_page import basepage

class LoginAPI(basepage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_api_login(self, api,  username, password):
        payload = {
            "username": username,
            "password": password
        }
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.get(api, json=payload, headers=headers)

        print("Status code:", response.status_code)
        print("Response text:", response.text)

        assert response.status_code == 200, "Login API failed"



