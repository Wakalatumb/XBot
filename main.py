from time import sleep
import pyperclip
from dotenv import load_dotenv
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 10

USER_ID = os.environ.get("USER_ID")
PASSWORD = os.environ.get("PASSWORD")
P_N = os.environ.get("P_N")

brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
brave_options = webdriver.ChromeOptions()
brave_options.binary_location = brave_path
brave_options.add_experimental_option("detach", True)



class InternetSpeedTwitterBot:
    def __init__(self,):
        self.driver = webdriver.Chrome(options=brave_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        sleep(2)
        button = self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a')
        button.click()

        sleep(50)
        self.up = self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.down,self.up)
        return self.down,self.up


    def tweet_at_provider(self):
        tweet = f"the internet is slow at {self.up}/{self.down}"
        self.driver.get("https://x.com/home")
        sleep(4)
        username = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        username.send_keys(USER_ID,Keys.ENTER)

        input("enter your number ")
        pyperclip.copy(P_N)


        sleep(8)
        password = self.driver.find_element(By.NAME,value="password")
        password.send_keys(PASSWORD,Keys.ENTER)

        sleep(5)
        post = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        post.send_keys(tweet)

        sleep(1)
        click = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        click.click()
        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
