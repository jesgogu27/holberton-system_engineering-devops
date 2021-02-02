#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv

if __name__ == "__main__":
    """returns information about his/her TODO list progress"""
    url1 = requests.get("https://jsonplaceholder.typicode.com/todos")
    url2 = requests.get("https://jsonplaceholder.typicode.com/users")
    to_do = url1.json()
    users = url2.json()

    name = ""
    total_t = 0
    finish_t = 0
    tasks = []

    for user in users:
        if user["id"] == int(argv[1]):
            name = user["name"]

    for arg in to_do:
        if arg["userId"] == int(argv[1]):
            total_t += 1
            if arg["completed"]:
                finish_t += 1
                tasks.append(arg["title"])

    print("Employee {} is done with tasks({}/{}):".format(
        name, finish_t, total_t))
    for task in tasks:
        print("\t {}".format(task))
