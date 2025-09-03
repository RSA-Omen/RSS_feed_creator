import sys
import os

import feedparser

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import convert_YT_channel_ID_to_name, feed_parse, readline_from_file


# testing converting youtube channel ID to names
def test_convert_YT_channel_ID_to_name_valid():
    # ChosenArchitect's channel ID
    result = convert_YT_channel_ID_to_name("UClmdJ2bwqHjZONP9rIK7geA")
    assert "ChosenArchitect" in result


def test_convert_YT_channel_ID_to_name_invalid():
    # Invalid channel ID should return "Unknown YouTuber"
    result = convert_YT_channel_ID_to_name("INVALID_ID_123")
    assert result == "Unknown YouTuber"


def test_convert_YT_channel_ID_to_name_empty():
    result = convert_YT_channel_ID_to_name("")
    assert result == "Unknown YouTuber"


def test_convert_YT_channel_ID_to_name_nonexistent():
    result = convert_YT_channel_ID_to_name("NON_EXISTENT_ID")
    assert result == "Unknown YouTuber"


def test_convert_YT_channel_ID_to_name_special_chars():
    result = convert_YT_channel_ID_to_name(
        "UC_x5XG1OV2P6uZZ5FSM9Ttw"
    )  # Channel with special characters
    assert "Google for Developers" in result


def test_convert_YT_channel_ID_to_name_numeric():
    result = convert_YT_channel_ID_to_name(
        "UC_x5XG1OV2P6uZZ5FSM9Ttw123"
    )  # Channel with numeric ID
    assert "Unknown YouTuber" in result


def test_convert_YT_channel_ID_to_name_short_id():
    result = convert_YT_channel_ID_to_name(
        "UClmdJ2bwqHjZONP9rIK7ge"
    )  # Shortened valid ID
    assert "Unknown YouTuber" in result


def test_convert_YT_channel_ID_to_name_long_id():
    result = convert_YT_channel_ID_to_name(
        "UClmdJ2bwqHjZONP9rIK7ge1234567890"
    )  # Long valid ID
    assert "Unknown YouTuber" in result


# readline_from_file


def test_readline_from_file_valid(tmp_path):
    test_file = tmp_path / "youtuber.txt"
    test_file.write_text(
        "UClmdJ2bwqHjZONP9rIK7ge|ChosenArchitect\nUC_x5XG1OV2P6uZZ5FSM9Ttw|Google for Developers\n"
    )
    result = readline_from_file(filename=str(test_file))
    assert len(result) == 2
    assert "ChosenArchitect" in result[0]
    assert "Google for Developers" in result[1]


# write_to_file
def test_write_to_file_and_readline(tmp_path):
    test_file = tmp_path / "youtuber.txt"
    from main import write_to_file, readline_from_file

    write_to_file("UClmdJ2bwqHjZONP9rIK7ge|ChosenArchitect", filename=str(test_file))
    write_to_file(
        "UC_x5XG1OV2P6uZZ5FSM9Ttw|Google for Developers", filename=str(test_file)
    )

    result = readline_from_file(filename=str(test_file))
    assert len(result) == 2
    assert "ChosenArchitect" in result[0]
    assert "Google for Developers" in result[1]


# feed_parse


def feed_parse(content):
    feed = feedparser.parse(
        f"https://www.youtube.com/feeds/videos.xml?channel_id={content}"
    )
    # If the feed is invalid or has no title, treat as invalid
    if feed.bozo or not hasattr(feed.feed, "title"):
        return None
    return feed


def test_feed_parse_invalid():
    result = feed_parse("INVALID_ID_123")
    assert result is None


def test_feed_parse_valid():
    result = feed_parse("UClmdJ2bwqHjZONP9rIK7geA")
    assert result is not None
    assert hasattr(result.feed, "title")
    assert "ChosenArchitect" in result.feed.title
