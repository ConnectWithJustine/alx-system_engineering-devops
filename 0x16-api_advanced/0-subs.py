#!/usr/bin/python3
"""
Requirements:
    Prototype: def number_of_subscribers(subreddit)
    If not a valid subreddit, return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
        A function that queries the Reddit api and returns
        the number of subscribers (not acrive users, total sub)
    """
    # Reddit API endpoint for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid potential issues
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 '
        'Safari/537.36'
    }

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            subreddit_data = response.json()

            # Extract the number of subscribers from the response
            subscribers_count = subreddit_data['data']['subscribers']

            return subscribers_count
        elif response.status_code == 404:
            # Invalid subreddit (not found)
            print(f"Subreddit '{subreddit}' not found.")
            return 0
        else:
            # Handle other HTTP error codes if needed
            print(f"Error: {response.status_code}")
            return 0

    except Exception as e:
        # Handle any exceptions that may occur during the request
        print(f"An error occurred: {e}")
        return 0
