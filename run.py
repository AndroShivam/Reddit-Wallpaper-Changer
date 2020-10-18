import sys
import main

subreddit_name = sys.argv[1]

print(f"Setting wallpaper from r/{subreddit_name}...")

wallpaper = main.set_wallpaper(subreddit_name = subreddit_name)

print("Done!")

