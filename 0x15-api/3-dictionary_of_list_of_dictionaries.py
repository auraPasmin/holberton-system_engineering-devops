#!/usr/bin/python3
""" Exports data in the JSON format
"""
import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url).json()
    data = {}
    for user in users:
        todo = requests.get(url + '{}/todos'.format(user['id'])).json()
        data[user['id']] = [{
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': user['username']
            } for task in todo]

    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)
