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
    # Reddit API endpoint for getting the top posts of a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid potential issues
    headers = {'User-Agent': '/u/alx API Python for Holberton School'}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            subreddit_data = response.json()

            # Extract and print the titles of the first 10 hot posts
            for post in subreddit_data['data']['children']:
                print(post['data']['title'])

        elif response.status_code == 404:
            # Invalid subreddit (not found)
            print(
                    f"Subreddit '{subreddit}' not found. "
                    "Unable to retrieve posts.")
        else:
            # Handle other HTTP error codes if needed
            print(f"Error: {response.status_code}. Unable to retrieve posts.")

    except Exception as e:
        # Handle any exceptions that may occur during the request
        print(f"An error occurred: {e}. Unable to retrieve posts.")
