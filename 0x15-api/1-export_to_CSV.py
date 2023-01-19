#!/usr/bin/python3
"""returns information for a given employee ID"""
import csv
import requests
from sys import argv


def to_csv():
    """return API data"""
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for user in users.json():
        if user.get('id') == int(argv[1]):
            USERNAME = (user.get('username'))
            break
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((todo.get('completed'),
                                      todo.get('title')))

    """export to csv"""
    filename = "{}.csv".format(argv[1])
    with open(filename, "w", encoding='utf8') as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in TASK_STATUS_TITLE:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})


if __name__ == "__main__":
    if len(argv) > 1:
        to_csv()
    else:
        print("You must add a UserId to select a file!")
