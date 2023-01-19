#!/usr/bin/python3
"""returns information for a given employee ID"""
import json
import requests
from sys import argv


def to_json():
    """method returns information on Employee"""
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    for user in users.json():
        """returns users as a json file"""
        if user.get('id') == int(argv[1]):
            USERNAME = (user.get('username'))
            break
    TASK_STATUS_TITLE = []

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    for todo in todos.json():
        """get a dictionary of todos"""
        if todo.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((todo.get('completed'),
                                      todo.get('title')))

        """export to json"""
        file = []
        for task in TASK_STATUS_TITLE:
            file.append({"task": task[1], "completed": task[0],
                         "username": USERNAME})
        data = {str(argv[1]): file}
        filename = "{}.json".format(argv[1])
        with open(filename, "w", encoding='utf8') as f:
            json.dump(data, f)


if __name__ == "__main__":
    if len(argv) > 1:
        to_json()
    else:
        print("You must add a UserId!")
