#!/usr/bin/python3
"""Exports all todo data to json
"""

import json
import requests

if __name__ == '__main__':
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    users = requests.get('{}/users'.format(BASE_URL)).json()

    with open('todo_all_employees.json', 'w', encoding='utf8') as f:
        output = {}
        for user in users:
            tasks = []
            for todo in requests.get('{}/todos'.format(BASE_URL),
                                     params={"userId": user.get("id")}).json():
                tasks.append({"username": user.get("username"),
                              "task": todo.get("title"),
                              "completed": todo.get("completed")})
            output[user.get("id")] = tasks
        json.dump(output, f)
