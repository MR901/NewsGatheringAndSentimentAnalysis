from selenium import webdriver
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