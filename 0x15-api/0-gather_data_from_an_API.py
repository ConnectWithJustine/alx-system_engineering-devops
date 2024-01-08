#!/usr/bin/python3
'''
python script that returns information using REST API
'''
import requests
from sys import argv


def get_employee_todo_progress(emp_id):
    # API endpoint for user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    # API endpoint for user's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_data = user_response.json()

        # Check if 'name' key is present in the response
        if 'name' in user_data:
            # Fetch TODO list for the user
            todo_response = requests.get(todo_url)
            todo_data = todo_response.json()
            # Filter completed tasks
            completed_tasks = [task for task in todo_data if task['completed']]

            # Display TODO list progress
            print(f"Employee {user_data['name']} is done with tasks "
                  f"({len(completed_tasks)}/{len(todo_data)}):")
            print(f"\t{user_data['name']}: {len(completed_tasks)} "
                  f"tasks completed out of {len(todo_data)}")

        # Display titles of completed tasks
            for task in completed_tasks:
                print(f"\t\t{task['title']}")
        else:
            print(f"Employee with ID {emp_id} not found.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(argv) > 1:
        emp_id = int(argv[1])
        get_employee_todo_progress(emp_id)
