
import time
from Api.news_feed_api import NewsFeedAPI
from Pages.login_page import LoginPage
from Tests.base_test import BaseTest
from Utils.config_reader import ConfigReader


class TestAPINewsFeed(BaseTest):
    def test_api_get_news(self):
        news_feed_api = NewsFeedAPI(self.driver)
        config = ConfigReader.load_config()
        
        news_feed_api.test_api_get_news(config.get_news_feed_api())

        self.teardown()

    def test_api_like_action(self):
        news_feed_api = NewsFeedAPI(self.driver)
        config = ConfigReader.load_config()
        
        news_feed_api.test_api_like_action(config.get_action_like_api())

        self.teardown()

    def test_new_feed_UI(self):
        login_page = LoginPage(self.driver)
        config = ConfigReader.load_config()
        
        time.sleep(5)
        self.allure_screenshot("login_success_screenshot")

        login_page.login(config.username, config.password)

        time.sleep(5)
        self.allure_screenshot("dashboard_screenshot")

        news_feed_api = NewsFeedAPI(self.driver)
        news_feed_api.click_new_feed_button()

        time.sleep(5)
        self.allure_screenshot("new_feed_button_clicked")

        news_feed_api.test_api_get_news(config.get_news_feed_api())

        self.teardown()


