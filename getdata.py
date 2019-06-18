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
import json
from googletrans import Translator
from urllib.request import urlopen
import pprint




translator = Translator()

def getQuotes(keyword):
    keyword_0=keyword

    # Initialize lists
    quoteArray = []
    authorArray = []
    pageNameArray = [keyword_0]
    base_url = "http://www.brainyquote.com/quotes/keywords/"
    url = base_url + keyword + ".html"
    response_data = requests.get(url).text[:]
    soup = BeautifulSoup(response_data, 'html.parser')

    if soup.find("div", {"class":"monk-box"}):
        # There is no page for this keyword...
        print("There are no quotes for this keyword!")
        print(keyword_0)
        exit()
    # Populate quoteArray
    for item in soup.find_all("a", class_="b-qt"):
        input_text = item.get_text().rstrip()
        #dest is the language to be translate, 
        #All options are available on google translate url requests as '&tl=es', 
        #in this case it will be translate to spanish, default english is dest=en
        output_text=translator.translate(input_text, dest='en')
        text=output_text.text
        double_quotes= '""'
        text=text.join(double_quotes)
        quoteArray.append(text)

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
        photoArray.append(item ['href'])

    
    photo_url = random.sample(photoArray, 1)[0]

    filename = downloader(photo_url, path)

    return filename


def downloader(url, path):
    try:
        time.sleep(10)
        r = requests.get(url, stream=True, timeout=30)
        if r.status_code == 200:
            print("Success!")
            with open(os.path.join(path, str(uuid.uuid4()) + '.jpg'), 'wb') as f:
                shutil.copyfileobj(r.raw, f)

                return f.name

    except Exception:
        print("There was an issue downloading the picture!")
        #logging.exception("error")



def getTags(keyword, smart_hashtags, keywords):


    if smart_hashtags == False :

        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets' )

        chrome_options = Options()
        #options.headless = True
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        print(path)
        browser = webdriver.Chrome(chrome_options = chrome_options,  executable_path = path + '/chromedriver')
        base_url = "https://www.all-hashtag.com/hashtag-generator.php"
        browser.get (base_url)

        user_field = browser.find_element_by_id("keyword")
        user_field.send_keys(keyword)
        user_field.submit()
        time.sleep (15)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        tags = soup.find ('div', class_ = 'copy-hashtags').text
        tagString = " ".join(tags.split())


    elif smart_hashtags == True :

        tags = keywords
        smart_tags = set_smart_hashtags(tags)
        smart_tags = ["#" + elem for elem in smart_tags]

        if len(smart_tags) > 20:
            smart_tags = random.sample(smart_tags, 20)
            tagString = " ".join(smart_tags)

        else:
            tagString = " ".join(smart_tags)

    return tagString





def set_smart_hashtags(tags, log_tags=True) :

        smart_hashtags = []

        """Generate smart hashtags based on https://displaypurposes.com/"""
        """ranking, banned and spammy tags are filtered out."""

        if tags is None:
            print('set_smart_hashtags is misconfigured')
            return

        for tag in tags:
            req = requests.get(
                u'https://d212rkvo8t62el.cloudfront.net/tag/{}'.format(tag))
            data = json.loads(req.text)

            if data['tagExists'] is True:
                random_tags = data['results']
                #random_tags = random.sample(data['results'],limit)
                for item in random_tags:
                    smart_hashtags.append(item['tag'])

                if log_tags is True:
                    for item in smart_hashtags:
                        print(u'[smart hashtag generated: {}]'.format(item))
            else:
                print(u'Too few results for #{} tag'.format(tag))

        # delete duplicated tags
        smart_hashtags = list(set(smart_hashtags))
        return smart_hashtags


