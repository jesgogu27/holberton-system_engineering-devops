 #!/usr/bin/python3
'''Count it'''
import requests
import sys


def search(subreddit, word):
    """ parses the title of all hot articles, and prints
    a sorted count of given keywords
    """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, word.get('after'))
    user_agent = {'User-Agent': 'dagute'}

    req = requests.get(url, headers=user_agent).json()

    if req.get('error') == 404:
        return (None)
    children = req.get('data').get('children')
    for arg in children:
        title = arg.get('data').get('title').lower().split(' ')
        for key, value in word.items():
            if key != 'after':
                word[key] += title.count(key)
    after = req.get('data').get('after')
    if after:
        word['after'] = after
        search(subreddit, word)
    else:
        for key, value in sorted(word.items()):
            if value is not 0 and key is not 'after':
                print("{}: {}".format(key, value))


def count_words(subreddit, word_list):
    """counts words in a subreddit"""
    word = {}
    for arg in word_list:
        word[arg] = 0
    word['after'] = ''
    search(subreddit, word)
