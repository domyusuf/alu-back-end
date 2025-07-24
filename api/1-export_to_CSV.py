#!/usr/bin/python3
"""Exports employee TODO list to CSV format."""

import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    # Fetch user details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url).json()
    username = user_response.get("username")

    # Fetch tasks
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos = requests.get(todos_url).json()

    # Write to CSV
    filename = f"{employee_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])
