# Scraper to grab Winterpark.com data, unsuccessful due to Incapsula error - Using Selenium 
# Side note: Cannot grab HTML but can find elements
import json
from data import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Setup to change browser options
options = Options()
options.add_argument('--window-size=1920, 1200')
# Comment below to run web browser, currently running Selenium without display
options.headless = True

def wp_data():
    # Selenium setup
    url = 'https://www.winterparkresort.com/the-mountain/mountain-report'
    driver = webdriver.Chrome(options=options, executable_path="c:\\chromedriver.exe")
    driver.get(url)

    # Grabbing Winter Park data via Xpath - selecting by id/class is tedious
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
    lifts = driver.find_element_by_xpath(
            '//*[@id="mountainConditionsApp"]/div[2]/div[2]/div/div[1]/div[2]/span'
                ).text
    trails = driver.find_element_by_xpath(
            '//*[@id="mountainConditionsApp"]/div[2]/div[2]/div/div[2]/div[2]/span'
            ).text

    driver.quit()

    # int conversion
    temp = int(temp.split('.',1)[0])
    depth_total = int(depth_total.split('.',1)[0])
    depth_overnight = int(depth_overnight.split('.',1)[0])
    lifts = int(lifts)
    trails = int(trails)    

    return data(temp, depth_total, depth_overnight, lifts, trails)




