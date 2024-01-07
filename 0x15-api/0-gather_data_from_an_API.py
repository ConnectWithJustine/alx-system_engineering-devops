#!/usr/bin/python3
'''
Python script that returns information using REST API
'''
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get(f"{url}users/{user}")
        name = req.json().get("name")
        if name is not None:
            json_req = requests.get(
                f"{url}todos?userId={user}").json()
            all_task = len(json_req)
            completed_task = []
            for t in json_req:
                if t.get("completed") is True:
                    completed_task.append(t)
            count = len(completed_task)
            print(f"Employee {name} is done with tasks({count}/{all_task}):")
            for title in completed_task:
                print("\t {}".format(title.get("title")))
