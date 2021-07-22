from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import time

chrome_driver_path = "C:\Develop\chromedriver.exe"

EMAIL = "Email"
PASSWORD = "Password"
SIMILAR_ACCOUNT = "modern.architect"

class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(EMAIL)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        button = self.driver.find_element_by_class_name("cmbtv")
        button.click()
        time.sleep(5)
        not_now = self.driver.find_element_by_class_name("HoLwm ")
        not_now.click()

    def find_followers(self):
        time.sleep(4)
        follower_find = self.driver.find_element_by_class_name("XTCLo")
        follower_find.send_keys("modern.architect")
        follow_account = self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

    def follow(self):
        time.sleep(5)
        to_follow = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        to_follow.click()
        time.sleep(2)
        scr1 = self.driver.find_element_by_class_name("isgrP")
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            time.sleep(2)

        gt_buttons = self.driver.find_elements_by_class_name("Pkbci")
        for i in gt_buttons:
            i.click()
            time.sleep(1)

bot = InstaFollower(chrome_driver_path)
bot.login()
bot.find_followers()
bot.follow()
