import json

class ConfigReader:
    def __init__(self, base_url, username, password, loginapi, newsFeedAPI, actionLikeAPI):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.loginapi = loginapi
        self.newsFeedAPI = newsFeedAPI
        self.actionLikeAPI = actionLikeAPI

    @staticmethod
    def load_config(path='url.json'):

        with open(path, 'r') as file:
            data = json.load(file)

        return ConfigReader(
            base_url=data["url"],
            username=data["username"],
            password=data["password"],
            loginapi=data["loginapi"],
            newsFeedAPI=data["newsFeedAPI"],
            actionLikeAPI=data["actionLike"]
        )
        
    
    def get_url(self):
        return self.base_url
    
    
    def get_username(self):
        return self.username
    
    
    def get_password(self):
        return self.password
    
    def get_login_api(self):
        return self.loginapi
    
    def get_news_feed_api(self):
        return self.newsFeedAPI
    
    def get_action_like_api(self):
        return self.actionLikeAPI
    