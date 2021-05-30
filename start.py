from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

import pickle
from inputs import LoginInfo

def setupDriver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    PATH ="webdrivers\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    return driver

def facebookLogin(driver, credentials):
    # switch to appropriate window
    email = driver.find_element_by_id("email")
    email.send_keys(credentials.email)
    password = driver.find_element_by_id("pass")
    password.send_keys(credentials.password)
    email.send_keys(Keys.RETURN)

def twitterLogin(driver, credentials):
    button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
    button.click()
    driver.implicitly_wait(2)
    email = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label')
    email.send_keys(credentials.email)
    driver.implicitly_wait(2)
    password = driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(7) > label')
    password.send_keys(credentials.password)
    driver.implicitly_wait(2)
    button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]')
    button.click()
    
if __name__ == "__main__":
    windowIndex = 0
    driver = setupDriver()
    with open('login_data.pkl', 'rb') as input:
        facebookInfo = pickle.load(input)
        twitterInfo = pickle.load(input)
    if(facebookInfo != None):
        if(len(driver.window_handles) == 1):
            driver.get("https://www.facebook.com")
        else:
            windowIndex += 1
            driver.execute_script("window.open('https://www.facebook.com');", '')
            driver.switch_to_window(driver.window_handles[windowIndex])
        facebookLogin(driver, facebookInfo)

    if(twitterInfo != None):
        time.sleep(15)
        if(len(driver.window_handles) == 0):
            driver.get("https://www.twitter.com")
        else:
            windowIndex += 1
            driver.execute_script("window.open('https://www.twitter.com');", '')
            driver.switch_to.window(driver.window_handles[windowIndex])
        twitterLogin(driver, twitterInfo)
