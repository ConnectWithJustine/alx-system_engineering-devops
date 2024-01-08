#!/usr/bin/python3
'''
python script that returns information using REST API
'''
import json
import requests
from sys import argv


def get_employee_todo_progress(empId):
    # API endpoint for user information
    userUrl = f"https://jsonplaceholder.typicode.com/users/{empId}"
    # API endpoint for user's TODO list
    todoUrl = f"https://jsonplaceholder.typicode.com/todos?userId={empId}"

    try:
        # Fetch user information
        userResponse = requests.get(userUrl)
        userData = userResponse.json()
        EMPLOYEE_NAME = userData.get('name')

        # Check if 'name' key is present in the response
        if name:
            # Fetch TODO list for the user
            todoResponse = requests.get(todoUrl)
            todoData = todoResponse.json()
            # Filter completed tasks
            completedTasks = [task for task in todoData if task['completed']]
            NUMBER_OF_DONE_TASKS = len(completedTasks)
            TOTAL_NUMBER_OF_TASKS = len(todoData)

            # Display TODO list progress
            print(f"Employee {EMPLOYEE_NAME} is done with tasks "
                  f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

        # Display titles of completed tasks
            for task in completedTasks:
                print(f"\t{task['title']}")
        else:
            print(f"Employee with ID {empId} not found.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(argv) > 1:
        empId = int(argv[1])
        get_employee_todo_progress(empId)
