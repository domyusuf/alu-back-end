#!/usr/bin/python3
"""Exports employee TODO list to CSV format"""

import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Fetch user data
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
    username = user.get("username")

    # Fetch todos
    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}").json()

    # Export to CSV
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                str(employee_id),
                username,
                str(task.get("completed")),
                task.get("title")
            ])
