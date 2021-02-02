#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests
from sys import argv


def json_format():
    """export data in the JSON format"""
    my_list = []
    emp_dict = {}

    url = "https://jsonplaceholder.typicode.com/"
    tasks = requests.get(url + "todos")
    tasks = tasks.json()
    users = requests.get(url + "users/")
    users = users.json()

    for user in users:
        for arg in tasks:
            if arg["userId"] == user["id"]:
                my_dict = {}
                my_dict["username"] = user.get("username")
                my_dict["task"] = arg["title"]
                my_dict["completed"] = arg["completed"]
                my_list.append(my_dict)
        emp_dict[user.get("id")] = my_list
        my_list = []
    file = "todo_all_employees.json"
    with open(file, 'w') as f:
        dump = json.dumps(emp_dict)
        f.write(dump)


if __name__ == "__main__":
    json_format()
