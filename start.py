from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import pickle
from inputs import LoginInfo

def setupDriver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    PATH ="webdrivers\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    return driver

def facebookLogin(driver):
    driver.get("https://www.facebook.com/")
    with open('login_data.pkl', 'rb') as input:
        facebookInfo = pickle.load(input)
    email = driver.find_element_by_id("email")
    email.send_keys(facebookInfo.email)
    password = driver.find_element_by_id("pass")
    password.send_keys(facebookInfo.password)
    email.send_keys(Keys.RETURN)

if __name__ == "__main__":
    driver = setupDriver()
    facebookLogin(driver)
