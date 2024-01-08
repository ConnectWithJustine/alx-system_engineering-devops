#!/usr/bin/python3

import requests

def get_employee_todo_progress(employee_id):
    # API endpoint for user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    # API endpoint for user's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_data = user_response.json()

        # Fetch TODO list for the user
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Filter completed tasks
        completed_tasks = [task for task in todo_data if task['completed']]

        # Display TODO list progress
        print(f"Employee {user_data['name']} is done with tasks "
              f"({len(completed_tasks)}/{len(todo_data)}):")
        print(f"\t{name}: {len(completed_tasks)} tasks completed out of {len(todo_data)}")

        # Display titles of completed tasks
        for task in completed_tasks:
            print(f"\t\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # You can replace the employee_id below with the desired ID when calling the script.
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)

