#!/usr/bin/python3
"""
Requirements:
    Prototype: def number_of_subscribers(subreddit)
    If not a valid subreddit, return 0.
"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """
        A function that queries the Reddit api and returns
        the number of subscribers (not acrive users, total sub)
    """
    user_agent = '/u/alx API Python for Holberton School'
    headers = {'user-agent': user_agent}

    # Reddit API endpoint for getting subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    client = requests.session()
    client.headers = headers

    response = client.get(url, allow_redirects=False)

    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0
