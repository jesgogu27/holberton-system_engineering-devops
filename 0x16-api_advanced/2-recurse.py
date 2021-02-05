#!/usr/bin/python3
"""Top Ten"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    prints the titles of the first 10 hot
    posts listed for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    user_agent = {'User-Agent': 'jesgogu27'}
    req = requests.get(url, headers=user_agent).json()

    if req.get('error') == 404:
        return (None)
    my_list = req.get('data').get('children')
    for num in my_list:
        hot_list.append(num.get('data').get('title'))
    after = req.get('data').get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
