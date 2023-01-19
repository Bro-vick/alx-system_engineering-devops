This is a readme for my tasks on api's

# Task 1. Export to CSV
This script is written in Python, it exports the tasks status and title of a specific user, given the user ID, to a CSV file.

The script starts by importing the necessary libraries which are "csv" and "requests". Then it defines a function named "to_csv()", which makes a GET request to two different endpoints of "http://jsonplaceholder.typicode.com" to get the user and task data of a specific user.

The first request is to "http://jsonplaceholder.typicode.com/users" to get the user data and it loops through all the users, checks if the user ID matches the user ID passed in as an argument (argv[1]), if it matches it takes the 'username' of that user and store it in 'USERNAME'.

The second request is to "http://jsonplaceholder.typicode.com/todos", to get all the task data of the users and it loops through all the tasks, checks if the 'userId' of the task matches the user ID passed in as an argument (argv[1]), if it matches it takes the 'completed' and 'title' of that task and appends it to the list named 'TASK_STATUS_TITLE'.

Then the script creates a CSV file with the name of user ID passed in as an argument, and writes the user ID, username, task completed status, and task title to the CSV file, by using the python csv library.

Finally, in the last if statement, it checks if any argument is passed when running the script, if not it prints "You must add a UserId to select a file!"

In summary, when this script is run with a user ID as an argument, it exports the tasks status and title of the user to a CSV file with the user ID passed in as the file name.

# Task 2. Export to JSON

This script is a python program that takes an employee ID as an argument, and returns information about that employee. Specifically, it retrieves data from two different endpoints of a mock RESTful API service: "https://jsonplaceholder.typicode.com/users" and "https://jsonplaceholder.typicode.com/todos".

It then uses this data to create a new JSON file, where it stores the information about the tasks and their completion status, as well as the username of the employee with the given ID. The file is saved with the name as the ID of the employee, in this format: "ID.json".

The code imports several modules, including json, requests, and argv from sys. It defines a function named "to_json()" which contains the main logic of the script. The function first makes a GET request to the "users" endpoint and loops through the returned JSON data to find the user with the ID passed as an argument. It then stores the username of that user in a variable.

Next, it makes a GET request to the "todos" endpoint, and loops through the returned JSON data to find all the tasks that belong to the user with the given ID. It then appends the completion status and title of each task to a list.

Finally, it creates a new dictionary with the format {'ID': [{'task': 'task name', 'completed': True/False, 'username': 'username'}]}, and then saves this dictionary to a new JSON file with the name ID.json, by using json.dump() method of json module.

It also has an if block at the end of the script, which checks if the user passed any argument, if not it will print "You must add a UserId!"
