#!/usr/bin/python3
""" Module gather data from an API
"""
import requests
from sys import argv as av


if __name__ == '__main__':
    # Of api
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(av[1])).json()
    todo = requests.get(url + 'users/{}/todos'.format(av[1])).json()
    tasks = [task.get('title') for task in todo if task.get('completed')]
    first = 'Employee {} is done with '.format(user['name'])
    first += 'tasks({}/{}):'.format(len(tasks), len(todo))

    print(first)
    [print('\t {}'.format(task)) for task in tasks]
