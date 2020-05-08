#!/usr/bin/python3
"""Module top ten
"""
from requests import *


def top_ten(subreddit):

    api = 'https://api.reddit.com/r/{}/hot?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Auramps'}
    r = get(api, headers=headers).json()
    try:
        [print(top['data']['title']) for top in r['data']['children']]
    except Exception:
        print(None)
