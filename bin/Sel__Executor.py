
import time, ast
from Sel1_LoadDriver import accessDriver
from Sel2_InitiateSearch import search
from Sel3a_GatherNews import gatherAllNewsAndSaveIt


def execute(config, msg = False):
    '''
    function to execute operations
    '''
    
    t0 = int(time.time())
    ## loading driver
    driver = accessDriver(config['useWhichBrowser']).getDriver() # option: 'Chrome', 'Mozilla', 'EDGE', ''    
    
    if msg:
        d = dict(driver.capabilities)
        print('Driver Configuration')
        for ele in d.keys():
            print(ele, ':', d[ele])
    time.sleep(2)
    t1 = int(time.time())
    
    ## Performing Search
    sea = search(driver, config['searchUsing']) # option: 'GoogleSearch', 'GoogleNewsSearch', 'GoogleScholarSearch', 'GoogleImageSearch'
    sea.searchAndOpenNewTab(config['searchFor'])
    time.sleep(2)
    t2 = int(time.time())
    
    ## Gathering Content
    #print(config['outputFilePath'], '----', config['searchFor'])
    outputFile = config['outputFilePath'].format(config['searchFor'])
    print(config['outputFilePath'], '----', config['searchFor'], '----', outputFile)
    if config['searchUsing'] == 'GoogleNewsSearch':
        gatherAllNewsAndSaveIt(driver, outputFile)
    t3 = int(time.time())
    
    driver.quit()
    print('||   Execution Complete   ||')
    print('')
    print('|\tTime Taken')
    print('|\t|\t> Load Driver:', t1-t0, 'sec')
    print('|\t|\t> Search Content:', t2-t1, 'sec')
    print('|\t|\t> Gather Content:', t3-t2, 'sec')
    print('')
    print('|\t|\t> Whole Execution Time:', t3-t0, 'sec')


def checkConfigAndTriggerSearch(config):
    '''
    Check if multiple search terms are shared or a single and then initiate search
    '''
    try:
        li = ast.literal_eval(config['searchFor'])
        if type(li) is list:
            for searchFor in li:
                tempConfig = config
                tempConfig['searchFor'] = searchFor
                execute(tempConfig)
        else:
            execute(config)
    except:
        execute(config)
        
    
if __name__=="__main__":
    
    configSearch = {
        'useWhichBrowser' : 'Chrome',
        # option: 'Chrome', 'Mozilla', 'EDGE', ''
        'searchUsing' : 'GoogleNewsSearch',
        ## 'GoogleSearch', 'GoogleNewsSearch', 'GoogleScholarSearch', 'GoogleImageSearch'
        'searchFor' : '''["Machine Learning", "Artificial Intelligence"]''',
        'outputFilePath' : '../data/output/ExtractedNews_{}.tsv'
    }
    
    checkConfigAndTriggerSearch(configSearch)
    
    