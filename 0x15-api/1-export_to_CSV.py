#!/usr/bin/python3
"""Export to CSV"""
import requests
from sys import argv
from csv import DictWriter, QUOTE_ALL


def export_csv(emp_id):
    """ export data in the CSV format"""
    output = ["userId", "username", "completed", "title"]
    with open("{}.csv".format(emp_id), 'w') as f:
        writer = DictWriter(f, fieldnames=output, quoting=QUOTE_ALL)
        for arg in to_do:
            if arg["userId"] == emp_id:
                del arg["id"]
                arg["username"] = name
                writer.writerow(arg)

if __name__ == "__main__":
    """returns information about his/her TODO list progress"""
    url1 = requests.get("https://jsonplaceholder.typicode.com/todos")
    url2 = requests.get("https://jsonplaceholder.typicode.com/users")
    to_do = url1.json()
    users = url2.json()

    name = ""
    completed = ""
    emp_id = ""
    tasks = []

    for user in users:
        if user["id"] == int(argv[1]):
            name = user["username"]

    export_csv(int(argv[1]))
