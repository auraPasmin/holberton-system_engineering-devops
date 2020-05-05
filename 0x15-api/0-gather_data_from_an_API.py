#!/usr/bin/python3
"""Write a Python script that, using this REST API
for a given employee ID
"""

import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    api = 'https://jsonplaceholder.typicode.com'
    user = requests.get(api+'/users/'+userId)

    name = user.json().get('name')

    all = requests.get(api+'/all')
    allTasks = 0
    completed = 0

    for task in all.json():
        if task.get('userId') == int(userId):
            allTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, allTasks))

    print('\n'.join(["\t " + task.get('title') for task in all.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
