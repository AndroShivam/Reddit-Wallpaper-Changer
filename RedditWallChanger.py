import ctypes
import os
import sys
import requests
import shutil
import praw
import random


def perform_auth():
    reddit = praw.Reddit(client_id = "your_client_id",
                        client_secret = "your_client_secret", 
                        user_agent = "user_agent",
                        username = "reddit_username", 
                        password = "reddit_password")
    return reddit

image_urls = []
def get_url_from_subreddit(subreddit_name):
    reddit = perform_auth()
    image_urls.clear()
    for submissions in reddit.subreddit(subreddit_name).hot(limit = 10):
        url = submissions.url
        image_urls.append(url)
    return image_urls[random.randint(0, 10)]

def set_wallpaper(subreddit_name):
    
    image_url = get_url_from_subreddit(subreddit_name)
    image_name = image_url.split('/')[-1]
    response = requests.get(image_url, stream = True)

    response.raw.decode_content = True

    if response.status_code == 200:
        with open(image_name, 'wb') as f:
            shutil.copyfileobj(response.raw, f)

        user_path = os.path.expanduser('~')
        image_path = os.path.join(user_path, 'Desktop', 'Stuff', image_name) # Specify the path where you have redditwallchanger.py and run.py

        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
    else:
       print("Something went wrong :(")
