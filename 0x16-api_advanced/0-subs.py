#!/usr/bin/python3
"""How many subs?"""
import requests


def number_of_subscribers(subreddit):

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "my name is Aura"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    try:
        return r.json().get("data").get("subscribers")
    except Exception:
        return 0
