import json
import os

class ConfigReader:
    _config = None

    @staticmethod
    def get_config():
        path =os.path.join(os.path.dirname(os.path.dirname(__file__)), "url.json")
        with open(path, "r") as file:
            return json.load(file)
        
    @staticmethod
    def get_url():
        return ConfigReader.load_config()['url']
    
    @staticmethod
    def get_usename():
        return ConfigReader.load_config()['usename']
    
    @staticmethod
    def get_password():
        return ConfigReader.load_config()['password']