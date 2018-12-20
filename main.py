from InstagramAPI import InstagramAPI
import schedule
import time
import random
import os
import datetime
from getdata import getQuotes, getPhotos, getTags, set_smart_hashtags

# *********************************************************************
# INPUT
# *********************************************************************
keywords = [
            'ocean', 'sea', 'keyword3'
            ]
username = ''
password = ''
foldername = 'pictures'
myproxy = ''
posting_hours = [12,13,14]

# *********************************************************************

def upload (username, password, myproxy, mycaption, myphoto):

    # upload
    try:
        api = InstagramAPI(username, password)
        api.setProxy(proxy= myproxy)
        api.login()
        api.uploadPhoto(myphoto, caption=mycaption)
        
        #remove photo
        os.remove(myphoto)
        
        print('posted!!')
    
    except :
        print('failed to upload')
    

if __name__ == '__main__':

    # set keyword
    keyword  = random.sample(keywords,1)[0]

    # get data
    smart_hashtags = True
    mytags = getTags (keyword, smart_hashtags, keywords)
    myphoto = getPhotos (keyword, foldername)
    myquote = getQuotes(keyword)
    
    #create caption
    mycaption =  myquote + '\n.\n.\n.\n.\n.\n' + mytags

    # get today date
    nowtime = datetime.datetime.now()
    year = nowtime.year
    month = nowtime.month
    day = nowtime.day

    # set the posting time
    p_hour = random.sample(posting_hours,1)[0]
    p_minute = random.randint(10,59)
    ptime1 = datetime.datetime(year, month, day, p_hour, p_minute)

    print ('\nposting time: ', ptime1)
    print('\nmycaption: ' , mycaption)
    print('\nmyphoto: ' , myphoto)
    #upload (username, password, myproxy, mycaption, myphoto)
    while True :
        
        nowtime = datetime.datetime.now()

        if nowtime >= ptime1 :
            
            upload(username, password, myproxy, mycaption, myphoto)
            break
        
        else:
            time.sleep(1)

