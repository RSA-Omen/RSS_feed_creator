import requests
import feedparser
from dateutil import parser as date_parser
from datetime import datetime, timedelta, timezone
youtuberfile = "youtuber.txt"

def write_to_file(content):
    with open(youtuberfile, 'a') as f:
        f.write(content + '\n')

def readline_from_file():
    with open(youtuberfile, 'r') as f:
        return f.readlines()
    
def convert_YT_channel_ID_to_name(content):
    feed = feed_parse(content)
    if feed and 'title' in feed.feed:
        return feed.feed.title
    return "Unknown YouTuber"

def feed_parse(content):
    feed = feedparser.parse(f'https://www.youtube.com/feeds/videos.xml?channel_id={content}')
    return feed

while True:
    msg="\n1.follow new youtuber\n2.view current youtuber list\n3.check new videos\n4.exit"
    option = input(f"{msg}\nChoose an option (1-4): ")
    
    if option == "1":
        new_yt = input("Enter the YouTuber's channel ID: ")
        new_yt_name = convert_YT_channel_ID_to_name(new_yt)
        print(f"Following new YouTuber: {new_yt_name}")
        # Store as "channel_id|channel_name"
        write_to_file(f"{new_yt}|{new_yt_name}")
    elif option == "2":
        # View current YouTuber list
        yt_list = readline_from_file()
        print("Current YouTubers:")
        for yt in yt_list:
            # Each line is "channel_id|channel_name"
            yt = yt.strip().split("|")
            if len(yt) == 2:
                channel_id, author = yt
                print(f"- {author} with code ({channel_id})")
            elif len(yt) == 1:
                print(f"- {yt[0]} (Unknown YouTuber)")
            else:
                print(f"- Invalid entry: {'|'.join(yt)}")
    elif option == "3":
        yt_list = readline_from_file()
        print("Checking new feed for YouTubers:")
        for yt in yt_list:
            yt = yt.strip().split("|")
            if len(yt) == 2:
                channel_id, author = yt
                feed = feed_parse(channel_id)
                if not feed or not feed.entries:
                    print(f"No valid feed found for: {author} ({channel_id})")
                    continue
                print(f"Checking new videos for: {author} ({channel_id})")
                cutoff = datetime.now(timezone.utc) - timedelta(hours=24)
                found = False
                for entry in feed.entries:
                    published_dt = date_parser.parse(entry.published)
                    if published_dt > cutoff:
                        found = True
                        print(getattr(entry, "author", author))
                        print(entry.link)
                        print(entry.title)
                        print(entry.link)
                        print(entry.published)
                        print("---")
                if not found:
                    print("No new videos in the last 24 hours.")
                print("---")
            elif len(yt) == 1:
                print(f"- {yt[0]} (Unknown YouTuber)")
            else:
                print(f"- Invalid entry: {'|'.join(yt)}")
    elif option == "4":
        print("Exiting...")
        exit()


#testdata
#UCXw1ddyrUmib3zmCmvSI1ow       -> Best ever Food Review Show
#UClmdJ2bwqHjZONP9rIK7geA       -> Chosen Architect

'''
feed = feedparser.parse('https://www.youtube.com/feeds/videos.xml?channel_id=UClmdJ2bwqHjZONP9rIK7geA')

# Calculate cutoff: now (UTC) minus 24 hours
cutoff = datetime.now(timezone.utc) - timedelta(hours=24)

for entry in feed.entries:
    published_dt = date_parser.parse(entry.published)
    if published_dt > cutoff:
        print(entry.title)
        print(entry.link)
        print(entry.published)
        print("---")
        '''