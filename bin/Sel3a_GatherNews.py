
import pandas as pd, time


def getArticleInfo(driver, artNo):
    '''
    Get the article info from the news portal
    '''
    source = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[1]/div/main/c-wiz/div[1]/div[{}]/div/article/div[2]/div/div'.format(artNo)
    time = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[1]/div/main/c-wiz/div[1]/div[{}]/div/article/div[2]/div/time'.format(artNo)
    heading = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[1]/div/main/c-wiz/div[1]/div[{}]/div/article/div[1]/div/h3/a/span'.format(artNo)
    story = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[1]/div/main/c-wiz/div[1]/div[{}]/div/article/div[1]/div/p'.format(artNo)
    url = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[1]/div/main/c-wiz/div[1]/div[{}]/div/article/a'.format(artNo)
    
    try:
        source = driver.find_element_by_xpath(source).text
    except Exception as e:
        print('Exception has occured:',e)
        source = None
    
    try:
        time = driver.find_element_by_xpath(time).get_attribute('datetime')
    except Exception as e:
        print('Exception has occured:',e)
        time = None
    
    try:
        heading = driver.find_element_by_xpath(heading).text
    except Exception as e:
        print('Exception has occured:',e)
        heading = None
    
    try:
        story = driver.find_element_by_xpath(story).text
    except Exception as e:
        print('Exception has occured:',e)
        story = None
    
    try:
        url = driver.find_element_by_xpath(url).get_attribute('href')
    except Exception as e:
        print('Exception has occured:',e)
        url = None
    
    artDict = {
        'source': source,
        'time': time,
        'heading': heading,
        'story': story,
        'url': url
    }
    return artDict

# print(getArticleInfo(driver, 2))
# print(getArticleInfo(driver, 3))
# print(getArticleInfo(driver, 4))



def gatherAllNewsAndSaveIt(driver, OutputFilePath):
    '''
    '''
    
    print('\n'+' +++++ '*7+'\n')
    check, articleNo = True, 0
    DF = pd.DataFrame(columns=['source', 'time', 'heading', 'story', 'url'])

    t0 = int(time.time())
    while check:
        articleNo += 1 
        tempDict = getArticleInfo(driver, articleNo)
        if (tempDict['source'] is None and tempDict['source'] is None and 
            tempDict['source'] is None and tempDict['source'] is None):
            check = False; break
        tempDF = pd.DataFrame(tempDict, index=[0])
        DF = DF.append(tempDF,ignore_index=True)
    t1 = int(time.time())
    print('|\tTime Taken :', t1-t0, 'sec')
    
    print('Output has a shape of:', DF.shape)
    DF.to_csv(OutputFilePath, sep='\t', index=False)
    print('Output has been saved at the location "'+OutputFilePath+'"')
    
    