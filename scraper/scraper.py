# Scraper to grab Winterpark.com data, unsuccessful due to Incapsula error - Using Selenium 
# Side note: Cannot grab HTML but can find elements
from WPData import *
from api import api
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Setup to change browser options
options = Options()
options.add_argument('--window-size=1920,1200')
# Comment below to run web browser, currently running Selenium without display
options.headless = True

# Selenium setup
url = 'https://www.winterparkresort.com/the-mountain/mountain-report'
driver = webdriver.Chrome(options=options, executable_path="c:\\chromedriver.exe")
driver.get(url)

# Grabbing data via Xpath - selecting by id/class is tedious
temp = driver.find_element_by_xpath(
    '//*[@id="mountainConditionsApp"]/div[2]/div[1]/div/div[3] \
    /div[2]/div[1]/div[1]/div[4]/div[1]/span'
    ).text
depth_total = driver.find_element_by_xpath(
    '//*[@id="mountainConditionsApp"]/div[2]/div[1]/div/div[3] \
    /div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]'
    ).text
depth_overnight = driver.find_element_by_xpath(
    '//*[@id="mountainConditionsApp"]/div[2]/div[1]/div/ \
    div[3]/div[2]/div[1]/div[2]/div[2]/div[3]/div[2]'
    ).text
depth_24 = driver.find_element_by_xpath(
    '//*[@id="mountainConditionsApp"]/div[2]/div[1]/div/div[3] \
    /div[2]/div[1]/div[2]/div[2]/div[4]/div[2]'
    ).text
depth_48 = driver.find_element_by_xpath(
    '//*[@id="mountainConditionsApp"]/div[2]/div[1]/div/div[3] \
    /div[2]/div[1]/div[2]/div[2]/div[5]/div[2]'
    ).text
lifts = driver.find_element_by_xpath(
    '//*[@id="mountainConditionsApp"]/div[2]/div[2]/div/div[1]/div[2]'
    ).text
trails = driver.find_element_by_xpath(
    '//*[@id="mountainConditionsApp"]/div[2]/div[2]/div/div[2]/div[2]'
    ).text

today_data = WPData(
    temp, depth_total, depth_overnight, 
    depth_24, depth_48, lifts, trails)

today_data.print()


