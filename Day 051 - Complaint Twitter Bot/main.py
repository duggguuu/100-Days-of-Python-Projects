# importing class

from TwitterBot import TwitterBot

# setting up webdriver

from selenium import webdriver
chrome_driver_path=r"C:\Users\ygohe\Desktop\Yash\Code\Development_Random\chromedriver.exe"

# setting up variables

promised_down=200
promised_up=10
twitter_id="wai_geee"
twitter_password="Crazy1234."

bot=TwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()

while True:
    pass