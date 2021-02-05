#!/usr/bin/python3
"""Top Ten"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot
    posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    user_agent = {'User-Agent': 'jesgogu27'}
    req = requests.get(url, headers=user_agent).json()

    if req.get('error') == 404:
        print('None')
        return

    my_list = req.get('data').get('children')
    for x, listed in enumerate(my_list[:10], 1):
        print(listed.get('data').get('title', None))
