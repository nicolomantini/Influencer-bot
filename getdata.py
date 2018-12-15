import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random
import time
import os
import uuid
import shutil



def getQuotes(keyword):

    # Initialize lists
    quoteArray = []
    authorArray = []
    pageNameArray = [keyword]

    base_url = "http://www.brainyquote.com/quotes/keywords/"
    url = base_url + keyword + ".html"
    response_data = requests.get(url).text[:]
    soup = BeautifulSoup(response_data, 'html.parser')

    # Populate quoteArray
    for item in soup.find_all("a", class_="b-qt"):
        quoteArray.append(item.get_text().rstrip())

    # Populate authorArray
    for item in soup.find_all("a", class_="bq-aut"):
        authorArray.append(item.get_text())

    # Create list of quotes
    ans = list (zip(quoteArray, authorArray))

    # get 1 random quote + author
    quote =   random.sample(ans,1)[0]
    myquote = quote [0] + ' - ' + quote [1]

    return myquote


def getPhotos(keyword, foldername):

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), foldername)
    
    photoArray = []

    base_url = "https://unsplash.com/search/photos/"
    url = base_url + keyword 
    response_data = requests.get(url).text[:]
    soup = BeautifulSoup(response_data, 'html.parser')

    for item in soup.findAll ('a', title = 'Download photo') :
        photoArray.append ( item ['href'])

    photo_url = random.sample(photoArray, 1)[0]

    filename = downloader(photo_url, path)

    return filename


def downloader(url, path):
    try:
        time.sleep(10)
        r = requests.get(url, stream=True, timeout=30)
        if r.status_code == 200:
            print("status code 200")
            with open(os.path.join(path, str(uuid.uuid4()) + '.jpg'), 'wb') as f:
                shutil.copyfileobj(r.raw, f)
                
                return f.name

    except Exception:
        print("status code not 200")
        #logging.exception("error")
    


def getTags(keyword):

    from selenium.webdriver.common.action_chains import ActionChains

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets' )

    options = Options()
    options.headless = True

    browser = webdriver.Chrome(chrome_options = options,  executable_path = path + '/chromedriver')
    base_url = "https://www.all-hashtag.com/hashtag-generator.php"
    browser.get (base_url)

    user_field = browser.find_element_by_id("keyword")
    user_field.send_keys(keyword)
    user_field.submit()
    time.sleep (15)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    tags = soup.find ('div', class_ = 'copy-hashtags').text
    tagString = " ".join(tags.split())
    
    return tagString


