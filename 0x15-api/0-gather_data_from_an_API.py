#!/usr/bin/python3
'''Gather data from an API'''
import requests
from sys import argv

if __name__ == '__main__':
    # Get employee response [used to get name in line 19]
    endpoint = 'https://jsonplaceholder.typicode.com'
    user_res = requests.get(endpoint + '/users/' + argv[1]).json()

    # this gets the total number of tasks [used to get len of all tasks in line 18]
    todos = requests.get(endpoint + '/todos?userId=' + argv[1]).json()

    # get number of completed tasks and their titles
    titles_done = [todo['title'] for todo in todos if todo['completed']]

    print('Employee {} is done with tasks({}/{}):'.format(user_res['name'], len(titles_done), len(todos)))
    
    [print('\t {}'.format(titles)) for title in titles_done]
