RSS Feed Generator.

A small python app that will check on feeds daily and create a watchlist. 
It will incorporate AI that will determine whether some watches overlap so you know which to avoid.
The main goal of the project is to stay informed without doomscrolling.

Features.
Fetches daily new releases using APIs.
feed a AI model with the data to determine what to watch.
create a summary with all the new info as well so the user can read without watching any of the feeds.
Create a nicely formatted textfile with hyperlinks.

sources:
youtube
watch-only website.
youtube music
spotify
twitch/kick streams

Porject Structire
RSS_Feed_Creator/
├── main.py
├── feeds
├── utils
├── tests
├── requirements.txt
└── README.md

packages in use:
    requests: Makes it easy to fetch data from the internet (like RSS feeds or APIs).
    feedparser: Reads and parses RSS/Atom feeds so you can work with news and updates.
    pytest: Lets you write and run tests to make sure your code works correctly.
    flake8: Checks your code for errors and style issues.
    black: Automatically formats your code to look neat and consistent.
    rich: Makes your terminal output colorful and adds features like tables and progress bars.
    colorama: Adds simple color to your terminal output (used by rich and other tools).
    python-dotenv: Loads secret settings (like API keys) from a hidden .env file.
    pydantic: Helps you check and validate your data using Python type hints.
    typing_extensions: Adds extra type hinting features for better code clarity.

Project Features
goal: create a daily dashboard from youtube, forums, youtube music playlist/podcasts. Can add extra platforms later, but for now create a dashboard for youtube. Add a AI model to read through these RSS feeds and make sure no content is duplicated. perhaps have a ordere , so if creator 1 does a video ona  trend, no need to show creator 2s video on the same trend. This will reduce the ammount of content to appear on the dashboard. 

Process
1. The user provides the channel IDs of their favorite content creators (e.g., YouTube channels).
2. The app adds each channel to a personalized watchlist. The user can arrange and prioritize this list as they prefer.
3. Each day, the app automatically checks all feeds in the watchlist for new content.
4. The app processes the feed data, removes duplicate or overlapping content using AI, and generates a clear daily report and dashboard for the user.
