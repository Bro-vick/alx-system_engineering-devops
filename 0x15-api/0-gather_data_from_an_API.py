#!/usr/bin/python3
'''Gather data from an API'''
import json
import sys
import urllib.request

def get_todo_list(employee_id):
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)
    response = urllib.request.urlopen(url)
    todo_list = json.loads(response.read())
    return todo_list

def get_employee_name(employee_id):
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = urllib.request.urlopen(url)
    employee = json.loads(response.read())
    return employee['name']

def print_todo_list(employee_id):

    todo_list = get_todo_list(employee_id)
    employee_name = get_employee_name(employee_id)
    done_tasks = [task for task in todo_list if task['completed']]
    total_tasks = len(todo_list)
    done_tasks_count = len(done_tasks)

    print(f'Employee {employee_name} is done with tasks({done_tasks_count}/{total_tasks}):')
    for task in done_tasks:
        print(f'\t{task["title"]}')


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    print_todo_list(employee_id)

