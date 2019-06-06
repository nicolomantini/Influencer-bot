import datetime, time
from post import prep_post, upload
import random
import requests


# *********************************************************************
# INPUT
# *********************************************************************
key = [
            'marketing','emprendedores'
            ]

keywords_photo = [
            'business-work',
            'coworking',
            'post-it',
            'mobile',
            'user-experience',
            'workshop',
            'small-business'
            ]

keywords_quote = [
            'small_business','strategy',
            'marketing',
            'innovation',
            'computers',
            'workshop',
            'enterprises',
            'information_technology',
            'new_technology','sales'
            ]


targets = key
number = 1
random_targets = targets
if len(targets) <= number:
    random_targets = targets
else:
    keywords = random.sample(targets, number)




username = 'colstorebot'
password = 'megafalcon12'
foldername = 'C:\\Users\\Wolf\\Desktop\\colstorefotos'
myproxy = ''



targets = keywords_photo
number = 1
random_targets = targets
if len(targets) <= number:
    photo_key = targets
else:
    photo_key = random.sample(targets, number)[0]




targets = keywords_quote
number = 1
random_targets = targets
if len(targets) <= number:
    quote_key = targets
else:
    quote_key = random.sample(targets, number)[0]


now = datetime.datetime.now()
day = int(now.strftime("%w"))
minute = int(now.strftime("%M"))
hour_now = int(now.strftime("%H"))
mon,tue,wed,thu,fri,sun = 1,2,3,4,5,0
window_post=True
posting_hours = hour_now

# Edit best hour to post, ie: 11, means best time to post is in between 11am-12pm recommend 2 hours morning and 2 hours for late
#if day == sun:
#   posting_hours=[23]
#elif day == mon: 
#    posting_hours=[12]

#elif day == tue:
#    posting_hours=[16]
#elif day == wed:
#    posting_hours=[11]
#elif day == thu:
#    posting_hours=[16]
#elif day == fri:
#    posting_hours=[13]
#else:
#    posting_hours=[18]

# *********************************************************************

#index = len(posting_hours)
#i=0
#while i < index:
#    if posting_hours[i] <= hour_now <= posting_hours[i]+1:

#        if hour_now < posting_hours[i]+1 and minute<=59:
#            window_post = True
#            break
#        break
#    i+= 1

if window_post is True:
    mycaption, myphoto = prep_post(keywords,photo_key,quote_key,foldername)
    upload(username, password, myproxy, mycaption, myphoto)
else:
    print("### Not in a window post interval, verify time for posting or script timing")
    pass

