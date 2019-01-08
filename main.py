from InstagramAPI import InstagramAPI
import schedule
import time
import random
import os
import datetime
from getdata import getQuotes, getPhotos, getTags, set_smart_hashtags
from PIL import Image
from resizeimage import resizeimage

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

    # lets make sure the image is the correct demensions
    # If the image is already 640x640 then it does nothing
    # If the image is not, it crops/scales to 640x640 by the middle
    # TODO: prevent resizing period if image is already the correct ratio to save resources
    # TODO: Figure out a better way of resizing to make sure the entire picture is included
    print("Resizing the image!")
    try:
        with open(myphoto, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_cover(image, [640, 640])
                cover.save(myphoto, image.format)
        print("Successfully resized the image!")
    except:
        print("Resizing Unsuccessful")

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
