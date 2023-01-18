import csv
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

def export_todo_list_to_csv(employee_id):
    todo_list = get_todo_list(employee_id)
    employee_name = get_employee_name(employee_id)
    csv_file = open('{}.csv'.format(employee_id), mode='w')
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
    for task in todo_list:
        csv_writer.writerow([employee_id, employee_name, task['completed'], task['title']])
    csv_file.close()

if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    export_todo_list_to_csv(employee_id)

