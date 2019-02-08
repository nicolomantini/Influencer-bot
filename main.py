import datetime, time
from post import prep_post, upload


# *********************************************************************
# INPUT
# *********************************************************************
keywords = [
            'ocean', 'sea', '
            ]
username = ''
password = ''
foldername = 'pictures'
myproxy = ''
posting_hours = [12,13,14]

# *********************************************************************

mycaption, myphoto, ptime = prep_post(keywords, posting_hours, foldername)

while True :

        nowtime = datetime.datetime.now()

        if nowtime >= ptime :

            upload(username, password, myproxy, mycaption, myphoto)
            break

        else:
            time.sleep(1)