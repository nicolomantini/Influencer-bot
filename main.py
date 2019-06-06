import datetime, time
from post import prep_post, upload
import random
import requests


# *********************************************************************
# INPUT
# *********************************************************************

username = ''
password = ''
foldername = ''
myproxy = ''

# tags generator
key = [
            'marketing','emprendedores'
            ]
# photo keywords options
keywords_photo = [
            'business-work',
            'coworking',
            'post-it',
            'mobile',
            'user-experience',
            'workshop',
            'small-business'
            ]
# quote keywords options
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

# *********************************************************************
# Random keywords
# *********************************************************************
targets = key
number = 1
random_targets = targets
if len(targets) <= number:
    random_targets = targets
else:
    keywords = random.sample(targets, number)

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

# *********************************************************************
# Now posting...control action via Cronjobs or Windows Task
# *********************************************************************
mycaption, myphoto = prep_post(keywords,photo_key,quote_key,foldername)
upload(username, password, myproxy, mycaption, myphoto)


