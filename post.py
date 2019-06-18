from InstagramAPI import InstagramAPI
from PIL import Image
from resizeimage import resizeimage
import schedule
import time, datetime
import random, os
from getdata import getQuotes, getPhotos, getTags, set_smart_hashtags


def prep_post (keywords,photo_key,quote_key,foldername) :
    
    # set keyword
    keyword  = random.sample(keywords,1)[0]

    # get data
    smart_hashtags = True
    mytags = getTags (keyword, smart_hashtags, keywords)
    myphoto = getPhotos (photo_key, foldername)
    myquote = getQuotes(quote_key)

    #create caption
    mycaption =  myquote + '\n.\n.\n.\n.\n.\n' + mytags

    # get today date
    nowtime = datetime.datetime.now()
    year = nowtime.year
    month = nowtime.month
    day = nowtime.day

    # set the posting time
    #p_hour = random.sample(posting_hours,1)[0]
    #p_minute = random.randint(10,59)
    #ptime = datetime.datetime(year, month, day, p_hour, p_minute)

    #print ('\nThe photo will be posted at: ', ptime)
    print('\nYour Caption: ' , mycaption)
    print('\nThe path for your photo: ' , myphoto)
#    upload (username, password, myproxy, mycaption, myphoto)

    return mycaption, myphoto


def upload (username, password, myproxy, mycaption, myphoto):

    # lets make sure the image is the correct demensions
    # If the image is already 640x640 then it does nothing
    # If the image is not, it crops/scales to 640x640 by the middle
    # TODO: prevent resizing period if image is already the correct ratio to save resources
    # TODO: Figure out a better way of resizing to make sure the entire picture is included
    # TODO: Perhaps create an option on how to handle images out of spec?

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
        # If they have set a proxy, lets use it... otherwise
        # Lets notify them and then continue without it.
        if myproxy: # proxy is not blank
            print("Using a proxy!")
            api.setProxy(proxy= myproxy)
        else:
            print("You are not using a proxy, this is not recommended!")
        api.login()
        api.uploadPhoto(myphoto, caption=mycaption)

        #remove photo
        #os.remove(myphoto)

        print('SUCCESS! Your photo has been posted!')

    except :
        print('FAILURE! Your photo was not posted!')


