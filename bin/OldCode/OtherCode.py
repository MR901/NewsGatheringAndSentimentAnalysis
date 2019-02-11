
# Packages
# pip3 install PyExecJS
# pip3 install selenium


## Importing Package
## Official Page: https://github.com/SeleniumHQ/selenium/tree/master/py
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
# from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from selenium.webdriver.common.keys import Keys
# import execjs
# import time, sys, glob

'''
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()
'''




# go to the google home page
driver.get("https://www.moneycontrol.com/news/commodities-news-94.html")
driver.find_element_by_id('search_str').send_keys('airtel')
driver.find_element_by_id("search_str").send_keys(Keys.ENTER)
a = driver.find_element_by_xpath("//a[contains(text(),'NEWS')]")
a.click() 
content = driver.find_elements_by_tag_name("strong")
# text = list()
# for i in range(0,40):
    
#     print content.text
#     if len(content.text) > 10:
#         text.append(content.text)
# element=driver.find_element_by_id("slider")
# dt = driver.find_element_by_tag_name("dt")
# print dt
# cl = element.find_element_by_partial_link_text("news")
# cl.click()
# time.sleep(10)
# news = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[3]/div[2]/div[11]/div[1]/div[2]/div[1]/dl[1]/dt[3]/a[1]")
# href = news.get_attribute('href')
# print hreffrom selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import execjs
import time
'''
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()
'''
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
#binary='/usr/bin/firefox'
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
# Create a new instance of the Firefox driver
#driver = webdriver.Firefox(binary)

binary = '/usr/bin/chromedriver'
driver =  webdriver.Chrome(binary,chrome_options = options)

# go to the google home page
driver.get("https://www.moneycontrol.com/news/commodities-news-94.html")
driver.find_element_by_id('search_str').send_keys('airtel')
driver.find_element_by_id("search_str").send_keys(Keys.ENTER)
a = driver.find_element_by_xpath("//a[contains(text(),'NEWS')]")
a.click() 
content = driver.find_elements_by_tag_name("strong")
# text = list()
# for i in range(0,40):
    
#     print content.text
#     if len(content.text) > 10:
#         text.append(content.text)
# element=driver.find_element_by_id("slider")
# dt = driver.find_element_by_tag_name("dt")
# print dt
# cl = element.find_element_by_partial_link_text("news")
# cl.click()
# time.sleep(10)
# news = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[3]/div[2]/div[11]/div[1]/div[2]/div[1]/dl[1]/dt[3]/a[1]")
# href = news.get_attribute('href')
# print href



## Other Resource

## Selenium Other Command
# driver.back()
# driver.fullscreen_window()
# driver.minimize_window()
# driver.maximize_window()
# driver.refresh()
# driver.save_screenshot(filename='TempScreenshot.png')

## Get All Active Windows/Tabs
activeHandles = driver.window_handles

## Switch Tabs
driver.switch_to.window(activeHandles[0])
driver.switch_to.window(activeHandles[1])

## Opens another Window
# driver.execute_script("window.open('https://www.yahoo.com')")

## Open New Tab
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL +"t")#+Keys.TAB) #Doesn't work
homeButton = driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div/div/div/div[2]/div[2]/div[1]/a')
NewTab = Keys.CONTROL + Keys.ENTER#+ 'T'
homeButton.send_keys(NewTab)
