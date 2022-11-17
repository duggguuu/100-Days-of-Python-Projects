import time

# setting up webdriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
chrome_driver_path=r"C:\Users\ygohe\Desktop\Yash\Code\Development_Random\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
url="https://tinder.com"
main_page=driver.current_window_handle # saving main page to switch back after popup
driver.get(url)

# finding google to login

login=driver.find_element(By.XPATH,'//*[@id="c-1560500889"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
time.sleep(5)

try:
    more=driver.find_element(By.XPATH,'//*[@id="c1006085331"]/main/div/div[1]/div/div/div[3]/span/button').click()
    time.sleep(5)
except NoSuchElementException:
    fb=driver.find_element(By.XPATH,'//*[@id="c1006085331"]/main/div/div[1]/div/div/div[3]/span/div[2]/button').click()
    time.sleep(5)

fb=driver.find_element(By.XPATH,'//*[@id="c1006085331"]/main/div/div[1]/div/div/div[3]/span/div[2]/button').click()
time.sleep(5)

# finding login page

for handle in driver.window_handles:
    if handle!=main_page:
        login_page=handle

# switching to popup

driver.switch_to.window(login_page)
time.sleep(5)

# logging in

uname=driver.find_element(By.ID,'email')
uname.send_keys("##username")
uname=driver.find_element(By.ID,'pass')
uname.send_keys("##password")
uname.send_keys(Keys.ENTER)

# switching back to main page

driver.switch_to.window(main_page)
time.sleep(5)

# defining swiping function

def swiping():
    try:
        like=driver.find_element(By.XPATH,'//*[@id="c-1560500889"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span').click()
        time.sleep(3)
    except NoSuchElementException:
        match_popup = driver.find_element_by_css_selector(".itsAMatch a").click()

# allowing and accepting things

try:
    location=driver.find_element(By.XPATH,'//*[@id="c1006085331"]/main/div/div/div/div[3]/button[1]').click()
    notifications=driver.find_element(By.XPATH,'//*[@id="c1006085331"]/main/div/div/div/div[3]/button[2]').click()
    allow_cookies=driver.find_element(By.XPATH,'//*[@id="c-1560500889"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]').click()
except NoSuchElementException:
    for n in range (100):
        swiping()

while True:
    pass