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

l = driver.find_element_by_class_name('temp-today').text
print(l) 