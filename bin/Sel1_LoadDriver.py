
from selenium import webdriver
import sys, glob
'''  '''
from pyvirtualdisplay import Display 
display = Display(visible=0, size=(800, 800))   ##to run it in background
display.start()

class accessDriver:
    
    def __init__(self, browser='Chrome'):
        self.whichBrowser = browser
        self.driverDir = '../data/driver/'
    
    def setOptionAndLoadDriver(self, path):
        '''
        To set the options/Configurations for the browser
        '''
        if self.whichBrowser == 'Chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument("--test-type")
            # options.add_argument("start-maximized");
            # options.add_argument("test-type");
            # options.add_argument("enable-strict-powerful-feature-restrictions");
            # options.add_argument("disable-geolocation");
            driver = webdriver.Chrome(executable_path=path, chrome_options = options)

        elif self.whichBrowser == 'EDGE':
            driver = webdriver.Edge(executable_path=path)

        elif self.whichBrowser == 'Mozilla':
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.cache.disk.enable", False)
            profile.set_preference("browser.cache.memory.enable", False)
            profile.set_preference("browser.cache.offline.enable", False)
            profile.set_preference("network.http.use-cache", False) 
            # profile.set_preference('browser.download.folderList', 2)
            # profile.set_preference('browser.download.manager.showWhenStarting', False)
            # profile.set_preference('browser.download.dir', os.getcwd())
            # profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv/xls')
            # profile.set_preference("geo.enabled", True)
            # profile.set_preference("geo.provider.use_corelocation", True)
            # profile.set_preference("geo.prompt.testing", False)
            # profile.set_preference("geo.prompt.testing.allow", False)
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(firefox_profile=profile, executable_path=path, firefox_options =  options)

        return driver
    
    
    def getDriver(self):
        '''
        This functions check for the environment and accordingly get the os, 
        After which it locates the driver file.
        File is loaded from another function

        returns the loaded driver file
        '''
        print('Loading '+self.whichBrowser)
        ## getting the browser
        if self.whichBrowser == 'Chrome':
            self.driverDir += 'chromedriver/'
        elif self.whichBrowser == 'EDGE':
            self.driverDir += 'edgedriver/'
        elif self.whichBrowser == 'Mozilla':
            self.driverDir += 'mozilladriver/'

        ## getting system os
        if 'linux' in sys.platform:
            self.driverDir += 'linux/'
        elif 'os' in sys.platform:
            self.driverDir += 'mac/'
        elif 'win' in sys.platform:
            self.driverDir += 'window/'

        print('Trying to locate the required driver at "'+ self.driverDir +'"')
        files =  glob.glob(self.driverDir+'*river*')
        print(files)
        if len(files) == 1:
            driver = self.setOptionAndLoadDriver(files[0])
            print('Driver file has been located and loaded')
        elif len(files) != 1:
            msg = 'Driver file hasn\'t been located and therefore can\'t be loaded.'
            print(msg); raise Exception(msg)

        return driver
    
# # option: 'Chrome', 'Mozilla', 'EDGE', ''
# driver = driver('Mozilla').getDriver()
# d = dict(driver.capabilities)
# print('Driver Configuration')
# for ele in d.keys():
#     print(ele, ':', d[ele])