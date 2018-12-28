# Influencer-bot
Instagram Influencer bot, that looks for pictures online and post them toghether with a caption.

# Usage
1. input your username, password, keywords, posting time, proxy, folder where to save pictures
2. add chromedriver to assets folder
3. run main.py

# How it works
Based on the list of keywords, the bot will choose a randome one and based on this one it will:
1) download a photo on unslpash.com
2) select a quote from brainyquotes.com
3) pick a list oh tags from all-hashtag.com.
4) if smart_hashtags is True, it generates a list of hashtags from displaypurposes.com

With all this material, it will create e post (photo + caption) and post it at a random time, within the list of posting hours.

For more info on the results you can check this article:
https://medium.com/xplor8/social-network-or-bot-network-1ec5839dd3c8

Enjoy!
/Nico
