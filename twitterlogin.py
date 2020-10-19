import time
from selenium import webdriver
import unittest

usr = input('Enter your name or email : ')
pwr = input('Enter your password : ')
image_path = input('Enter your image path : ')
msg = input('Enter your tweet : ')

class TwitterLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get("https://twitter.com/login")
        self.driver.find_element_by_name("session[username_or_email]").send_keys(usr)
        self.driver.find_element_by_name("session[password]").send_keys(pwr)
        self.driver.find_element_by_css_selector(".r-jwli3a").click()
        time.sleep(15)
        self.driver.find_element_by_css_selector("input.r-8akbif.r-orgf3d.r-1udh08x.r-u8s1d.r-xjis5s.r-1wyyakw").send_keys(image_path)
        self.driver.find_element_by_css_selector(".public-DraftStyleDefault-block").send_keys(msg)
        time.sleep(5)
        self.driver.find_element_by_css_selector("div.css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-1n0xq6e.r-1vuscfd.r-1dhvaqw.r-1ny4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr").click()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.refresh()
        time.sleep(10)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()