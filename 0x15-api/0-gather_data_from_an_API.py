#!/usr/bin/python3
"""returns information for a given employee ID"""
import requests
from sys import argv


def show_id():
    """method returns information on employee TODO list"""
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    for user in users.json():
        """returns users as a json file"""
        if user.get('id') == int(argv[1]):
            EMPLOYEE_NAME = (user.get('name'))
            break
    TOTAL_NUM_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    for todo in todos.json():
        """get a dictionary of todos"""
        if todo.get('userId') == int(argv[1]):
            TOTAL_NUM_OF_TASKS += 1
            if todo.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(todo.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUM_OF_TASKS))
    for task in TASK_TITLE:
        print("\t {}".format(task))


if __name__ == "__main__":
    if len(argv) > 1:
        show_id()
    else:
        print("You must add a UserId!")
