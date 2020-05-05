#!/usr/bin/python3
""" Module export to JSON
"""
import json
import requests
from sys import argv as av


if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(av[1])).json()
    todo = requests.get(url + 'users/{}/todos'.format(av[1])).json()
    data = {
        av[1]:
        [
            {
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': user['username']
            } for task in todo
        ]
    }
    file = '{}.json'.format(av[1])
    with open(file, 'w') as f:
        json.dump(data, f)
