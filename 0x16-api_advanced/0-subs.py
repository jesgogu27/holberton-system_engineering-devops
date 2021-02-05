#!/usr/bin/python3
"""How many subs"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers (not active users,
    total subscribers) for a given subreddit
    """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    User_Agent = {'User-agent': 'jesgogu27'}
    req = requests.get(url, headers=User_Agent).json().get('data')

    if req is None:
        return 0
    return req.get('subscribers')
