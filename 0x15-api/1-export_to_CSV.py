#!/usr/bin/python3
'''
    Python script that export data in the CSV format
'''
import requests
import sys
import csv


def FETCH_EMPLOYEE_TODO_PROGRESS(empId):
    # API endpoint for fetching user data
    USER_URL = f'https://jsonplaceholder.typicode.com/users/{empId}'
    # API endpoint for fetching TODO data
    TODO_URL = f'https://jsonplaceholder.typicode.com/todos?userId={empId}'

    # Fetching user data
    USER_RESPONSE = requests.get(USER_URL)
    USER_DATA = USER_RESPONSE.json()

    # Fetching TODO data
    TODO_RESPONSE = requests.get(TODO_URL)
    TODO_DATA = TODO_RESPONSE.json()

    # Extracting relevant information
    EMPLOYEE_NAME = USER_DATA['name']
    USER_ID = USER_DATA['id']
    TOTAL_TASKS = len(TODO_DATA)
    COMPLETED_TASKS = [task for task in TODO_DATA if task['completed']]

    # Exporting to CSV
    CSV_FILE_NAME = f"{USER_ID}.csv"
    with open(CSV_FILE_NAME, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                      'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Writing CSV header
        writer.writeheader()

        # Writing CSV rows
        for task in TODO_DATA:
            writer.writerow({
                'USER_ID': USER_ID,
                'USERNAME': EMPLOYEE_NAME,
                'TASK_COMPLETED_STATUS': 'completed' if task['completed']
                else 'not completed',
                'TASK_TITLE': task['title']
            })

    print(f"\nData exported to {CSV_FILE_NAME}")


if __name__ == "__main__":
    # Check if the script is provided with an employee ID
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    EMPLOYEE_ID = int(sys.argv[1])
    FETCH_EMPLOYEE_TODO_PROGRESS(EMPLOYEE_ID)
