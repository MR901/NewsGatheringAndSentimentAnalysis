
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import execjs
import time, sys, glob


class search:
    
    def __init__(self, driver, searchIn = 'GoogleSearch'):
        '''
        Search In Options: 'GoogleSearch', 'GoogleNewsSearch', 'GoogleScholarSearch', 'GoogleImageSearch'
        '''
        self.driver = driver
        self.searchIn = searchIn
        self.SearchConfig = {
            'GoogleSearch': {
                'URL': 'https://www.google.com/',
                'SearchBox_xPath': '/html/body/div/div[3]/form/div[2]/div/div[1]/div/div[1]/input',
                'OpenInNewLink': 'pnnext'
                },
            'GoogleNewsSearch':{
                'URL': 'https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en',
                'SearchBox_xPath': '/html/body/div[6]/div[2]/header/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]'
                },
            'GoogleScholarSearch':{
                'URL': 'https://scholar.google.co.in/',
                'SearchBox_xPath': '//*[@id="gs_hdr_tsi"]'
                },
            'GoogleImageSearch':{
                'URL': 'https://www.google.com/imghp?hl=EN',
                'SearchBox_xPath': '/html/body/div/div[3]/div[3]/form/div[2]/div/div[1]/div/div[1]/input'
                }
            }
        self.wait = WebDriverWait(driver, timeout= 60) 
        
    
    def genEleMsg(self, elem=None):
        '''
        to Generate Respeccted Msg when a element is loaded
        '''
        print('\n'+' ***** '*7+'\n')
        if elem is not None:
            print('Element visiblity:', elem.is_displayed())
            print('Element is at: ', elem.location) #Alternative gSearch.rect 
            print('Window is positioned at:', self.driver.get_window_rect())

        tabId = self.driver.current_window_handle
        CurrURL = self.driver.current_url
        print('Current Tab ID:',tabId, '\nCurrent URL:', CurrURL)
        return tabId, CurrURL

    
    def searchFromStart(self, which, searchFor = None):
        '''
        Start Search on google for the string  from the starting URL

        return an element id that can be opened in new tab
        '''
        url = self.SearchConfig[which]['URL']
        searchBox_xPath = self.SearchConfig[which]['SearchBox_xPath']
        
        ## Load the URL
        self.driver.get(url)

        ## Wait till element on the page that is loaded, Appears
        self.wait.until(EC.presence_of_element_located((By.XPATH, searchBox_xPath)))

        ## Perform Operation on Element
        ### click on element > Clear it > type "searchFor" > click 'ENTER'
        search = self.driver.find_element_by_xpath(searchBox_xPath)
        tabID_t1, URL_t1p1 = self.genEleMsg(search)
        search.click()
        search.clear()
        if searchFor is not None:
            print('Searching for "'+searchFor+'"')
            search.send_keys(searchFor) 
            search.send_keys(Keys.ENTER)


    def searchAndOpenNewTab(self, searchFor, activeOnNew = True, searchedContentOnRight =True):
        '''
        Input
        searchFor : a string that is to be search on google, 
        searchIn : search for context in 'Google' , 'News', '', 
        activeOnNew : Screen that should be active when the funtion has executed
        searchedConOnRightAndMoreRequest : if True, content is searched on the new tab i.e. to right of current Tab (more requests are made)
                                            if False, content is searched in current tab i.e. in left to the new tab (less Requests are made)
        -----searchedConOnRightAndMoreRequest=True : 8.51 s ± 1.66 s per loop (mean ± std. dev. of 7 runs, 1 loop each),
                                                        13.13 s ± 6.15 s per loop (mean ± std. dev. of 7 runs, 1 loop each),

        -----searchedConOnRightAndMoreRequest=False : 12.5 s ± 5.41 s per loop (mean ± std. dev. of 7 runs, 1 loop each),
                                                        19.5 s ± 16 s per loop (mean ± std. dev. of 7 runs, 1 loop each)
        returns newer_tab_handle and initial_tab_handle

        Issue: open in new tab is not working also CTRL + T is also not working
        '''
        searchInWhich = self.searchIn
        elemOpenNewLink = self.SearchConfig['GoogleSearch']['OpenInNewLink']
        
        NewTab = Keys.CONTROL + Keys.ENTER#+ 'T'
        
        ## Get All Active Windows/Tabs
        activeHandles_ini = self.driver.window_handles

        # <-----------------<<  Tab1  >>-----------------> #
        self.searchFromStart('GoogleSearch', searchFor)
        
        ## Wait till element on the page that is loaded, Appears
        self.wait.until(EC.presence_of_element_located((By.ID, elemOpenNewLink)))
        ## Perform Operation on Element
        elem = self.driver.find_element_by_id(elemOpenNewLink)
        tabID_t1, URL_t1p2 = self.genEleMsg(elem)
        elem.send_keys(NewTab)
        self.driver.switch_to.window(tabID_t1)
        
        ## Content on Current Page
        if searchedContentOnRight:
            ## getting google search screen
            self.searchFromStart(searchInWhich)
        else:
            ## getting Searched content 
            self.searchFromStart(searchInWhich, searchFor)

        # <-----------------<<  Tab2  >>-----------------> #
        ## Get All Active Windows/Tabs
        activeHandles_lat = self.driver.window_handles
        tabID_t2 = [ ele for ele in activeHandles_lat if ele not in activeHandles_ini ][0]
        ## Switch Tabs
        self.driver.switch_to.window(tabID_t2)

        ## Content on New Page
        if searchedContentOnRight:
            ## getting Searched content 
            self.searchFromStart(searchInWhich, searchFor)
        else:
            ## getting google search screen
            self.searchFromStart(searchInWhich)

        ## changing the active tab
        if activeOnNew is False:
            self.driver.switch_to.window(tabID_t1)

        return {'NewTab': tabID_t2, 'OldTab':tabID_t1}

# A = search('GoogleImageSearch') ## 'GoogleSearch', 'GoogleNewsSearch', 'GoogleScholarSearch', 'GoogleImageSearch'
# A.searchAndOpenNewTab('Abstract')