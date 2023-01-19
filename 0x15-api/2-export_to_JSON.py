#!/usr/bin/python3
"""returns information for a given employee ID"""
import json
import requests
from sys import argv

def to_json():
    """method returns information on Employee"""
    #GET request to the "users" endpoint
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    if users.status_code != 200:
        print("Unable to fetch user data. Please check the API endpoint")
        return
    user = next((user for user in users.json() if user.get('id') == int(argv[1])), None)
    if not user:
        print(f"User with ID {argv[1]} not found.")
        return
    USERNAME = user.get('username')
    TASK_STATUS_TITLE = []

    #GET request to the "todos" endpoint
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    if todos.status_code != 200:
        print("Unable to fetch task data. Please check the API endpoint")
        return
    #get a dictionary of todos
    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((todo.get('completed'), todo.get('title')))
    if not TASK_STATUS_TITLE:
        print(f"No tasks found for user ID {argv[1]}.")
        return

    #export to json
    file = []
    for task in TASK_STATUS_TITLE:
        file.append({"task": task[1], "completed": task[0], "username": USERNAME})
    data = {str(argv[1]): file}
    filename = f"{argv[1]}.json"
    with open(filename, "w", encoding='utf8') as f:
        json.dump(data, f)
    print(f"Correct USER_ID: OK")

if __name__ == "__main__":
    if len(argv) > 1:
        to_json()
    else:
        print("You must add a UserId!")

