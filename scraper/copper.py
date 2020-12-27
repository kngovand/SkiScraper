# Scraper to grab Copper data using Selenium 
# Side note: Cannot grab HTML but can find elements
from data import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Setup to change browser options
options = Options()
options.add_argument('--window-size=1920, 1200')
# Comment below to run web browser, currently running Selenium without display
options.headless = True

def copper_data():
    # Selenium setup
    url = 'https://www.coppercolorado.com/the-mountain/conditions-weather/snow-report'
    driver = webdriver.Chrome(options=options, executable_path="c:\\chromedriver.exe")
    driver.get(url)

    # Grabbing Copper data via Xpath - selecting by id/class is tedious
    temp = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/primary-header/div/nav/div[1]/\
            feeds-list/ul/li[1]/button/div[1]/widget-weather/div/span'
        ).text
    depth_total = driver.find_element_by_xpath(
        '//*[@id="main-content"]/cms-level0/section[2]/cms-level1/div[2]/section[2]/div[5]/\
        cms-level3/section/ui-section/div/div/dor-snow-report/div/div/dor-elm-loader/div/div/dor-grid/\
        div/div/div/dor-grid-item[1]/div/dor-grid/div/div/div/dor-grid-item[5]/div/div/h3'
        ).text
    depth_overnight = driver.find_element_by_xpath(
        '//*[@id="main-content"]/cms-level0/section[2]/cms-level1/div[2]/section[2]/div[5]/ \
        cms-level3/section/ui-section/div/div/dor-snow-report/div/div/dor-elm-loader/div/div/dor-grid/ \
        div/div/div/dor-grid-item[1]/div/dor-grid/div/div/div/dor-grid-item[1]/div/div/h3'
        ).text
    #Xpath for trails/lifts not working - going with class name "progress"    
    trails_lifts = driver.find_elements_by_class_name("progress")
    # class name "progress" returns multiple indexes, so 4 = lifts and 3 = trails
    # the index also returns multiple lines, so only grabbing first line using split()
    lifts = trails_lifts[4].text.split('\n')[0]
    trails = trails_lifts[3].text.split('\n')[0]

    driver.quit()

    # int conversion
    temp = int( ''.join(filter(str.isdigit, temp) ))
    depth_total = int( ''.join(filter(str.isdigit, depth_total) ))
    depth_overnight = int( ''.join(filter(str.isdigit, depth_overnight) ))
    lifts = int( ''.join(filter(str.isdigit, lifts) ))
    trails = int( ''.join(filter(str.isdigit, trails) ))

    return data(temp, depth_total, depth_overnight, lifts, trails)






