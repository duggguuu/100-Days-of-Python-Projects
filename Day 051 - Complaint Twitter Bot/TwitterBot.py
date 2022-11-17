from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:

    def __init__(self,driver_path):
        self.driver=webdriver.Chrome(executable_path=driver_path)

    def get_internet_speed(self):
        # self.driver.get(f"https://www.speedtest.net/")
        # self.driver.find_element(By.CLASS_NAME,'start-text').click()
        # time.sleep(60)

        # self.download=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        # print(f"download speed: {self.download}")

        # self.upload=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        # print(f"upload speed: {self.upload}")

        pass

    def tweet_at_provider(self):
        
        self.driver.get("https://twitter.com/login")
        time.sleep(5)

        self.uname=self.driver.find_element(By.NAME,'text').send_keys("wai_geee")
        self.next=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
        time.sleep(5)
        self.password=self.driver.find_element(By.NAME,'password').send_keys("Crazy1234..")
        self.next=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
        time.sleep(5)
        self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.COMMAND + 't')
        time.sleep(5)
        self.driver.get("https://twitter.com/intent/tweet?text=speed")
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]').click()