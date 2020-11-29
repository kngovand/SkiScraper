# Scraper to grab Winterpark.com data, unsuccessful due to Incapsula error - Using Selenium 
# Side note: Cannot grab HTML but can find elements

from bs4 import element
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Setting up Selenium
options = Options()
options.add_argument("--window-size=1920,1200")
# Run webdriver without browser
options.headless = True

url = 'https://www.winterparkresort.com/the-mountain/mountain-report#/'
driver = webdriver.Chrome(options=options, executable_path="c:\\chromedriver.exe")
driver.get(url)

# Grabbing data via Xpath - selecting by id/class is tedious
temp = driver.find_element_by_xpath('//*[@id="mountainConditionsApp"]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[1]/div[4]/div[1]/span').text
depth_total = driver.find_element_by_xpath('//*[@id="mountainConditionsApp"]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]').text
depth_overnight = driver.find_element_by_xpath('//*[@id="mountainConditionsApp"]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[3]/div[2]').text
depth_24 = driver.find_element_by_xpath('//*[@id="mountainConditionsApp"]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[4]/div[2]').text
depth_48 = driver.find_element_by_xpath('//*[@id="mountainConditionsApp"]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div[5]/div[2]').text
lifts = driver.find_element_by_xpath('//*[@id="mountainConditionsApp"]/div[2]/div[2]/div/div[1]/div[2]').text
trails = driver.find_element_by_xpath('//*[@id="mountainConditionsApp"]/div[2]/div[2]/div/div[2]/div[2]').text

print(temp + ' F')
print('Total: ' + depth_total)
print('Overnight: ' + depth_overnight)
print('24 hrs: ' + depth_24)
print('48 hrs: ' + depth_48)
print('Lifts open: ' + lifts)
print('Trails open: ' + trails)