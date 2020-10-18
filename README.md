<h1 align="center">Reddit Wallpaper Changer</h1>

## Screenshots
<p align="center">
<img src="https://github.com/AndroShivam/Reddit-Wallpaper-Changer/blob/main/screenshot1.png"/>
</p>
<br>
<p align="center">
<img src="https://github.com/AndroShivam/Reddit-Wallpaper-Changer/blob/main/screenshot2.png"/>
</p>

## Tech stack & Open-source libraries
- [PRAW](https://github.com/praw-dev/praw) - PRAW, an acronym for "Python Reddit API Wrapper", is a python package that allows for simple access to Reddit's API.

## How to Use
1. Create a Reddit App [here](https://www.reddit.com/prefs/apps)
2. add client_id , client_secret, user_agent, username, password to RedditWallChanger.py (client_id and client_secret from created app)
3. user_agent would be the name of app you created (Ex. user_agent = "testscript by u/shivam"})
4. change wallpaper download directory (os.path) in RedditWallChanger.py to where your both .py files are located.
5. open cmd in that directory and run 
```bash
python run.py subreddit_name
```
6. Enjoy!
