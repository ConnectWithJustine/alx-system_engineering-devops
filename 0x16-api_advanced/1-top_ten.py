#!/usr/bin/python3
"""
 Requirements:
    Prototype: def top_ten(subreddit)
    If not a valid subreddit, print None.
"""
import json
import requests


def top_ten(subreddit):
    """
        A function that queries the reddit api and prints the
        titles of the firs 10 hot posts listed for a given subreddit
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
