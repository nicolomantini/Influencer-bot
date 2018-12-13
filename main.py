from InstagramAPI import InstagramAPI
import schedule
import time
import random
import os
import inputdata
import datetime
from getdata import getQuotes, getPhotos, getTags

# *********************************************************************
# INPUT
# *********************************************************************
keywords = ['sea', 'ocean', 'dolphins', 'whales', 'shark']
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

    # get data
    keyword  = random.sample(keywords,1)[0]
    myphoto = getPhotos (keyword, foldername)
    myquote = getQuotes(keyword)
    mytags = getTags (keyword)
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

    while True :
        
        nowtime = datetime.datetime.now()

        if nowtime >= ptime1 :
            
            upload(username, password, myproxy, mycaption, myphoto)
            break
        
        else:
            time.sleep(1)

