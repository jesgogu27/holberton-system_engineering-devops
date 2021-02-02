#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
from sys import argv


def export_to_json(emp_id):
    """export to JSON"""
    my_list = []
    employee = {}

    url = "https://jsonplaceholder.typicode.com/"
    tasks = requests.get(url + "todos?userId=" + argv[1])
    tasks = tasks.json()
    emp = requests.get(url + "users/" + argv[1])
    emp = emp.json()
    USER_ID = emp.get("id")
    username = emp.get("username")

    for arg in tasks:
        my_dict = {}
        my_dict["task"] = arg["title"]
        my_dict["completed"] = arg["completed"]
        my_dict["username"] = username
        my_list.append(my_dict)

    employee[argv[1]] = my_list
    file = argv[1] + ".json"
    with open(file, 'w') as f:
        d = json.dumps(employee)
        f.write(d)

if __name__ == '__main__':
    export_to_json(argv[1])
