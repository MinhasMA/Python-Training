import selenium as sel
from selenium import webdriver
import time as tm
from selenium.webdriver.common.keys import Keys


class twitterbot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot()
        bot.get('https://twitter.com/')
        tm.sleep(3)
        email = bot.find_element_by_class_name('email-input')

mann = twitterbot('krishsharmavan@gmail.com', 'Tw13')
mann.login()



