import sys
import RedditWallChanger

subreddit_name = sys.argv[1]

print(f"Setting wallpaper from r/{subreddit_name}...")

wallpaper = RedditWallChanger.set_wallpaper(subreddit_name = subreddit_name)

print("Done!")

