from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = "/Users/sash/Documents/App-Brewery/Resources/chrome-webdriver/chromedriver"
TRAVEL_ACCOUNT = "travel"
USERNAME = "programmer.sachish@gmail.com"
PASSWORD = "Test54321"


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get(url="https://www.instagram.com/")
        time.sleep(5)
        username = self.driver.find_element_by_name("username")
        username.send_keys(USERNAME)
        password = self.driver.find_element_by_name("password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.RETURN)



    def find_followers(self):
        time.sleep(5)
        self.driver.get(url=f"https://www.instagram.com/{TRAVEL_ACCOUNT}/")
        time.sleep(2)

        follower = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        follower.click()
        time.sleep(2)

        follower_popup = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        for i in range(4):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_popup)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()



insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
