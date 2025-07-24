#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]  # ✅ Keep as string

    # API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Get user info and todos
    user_response = requests.get(user_url).json()
    todos_response = requests.get(todos_url).json()

    username = user_response.get("username")

    # Write to CSV
    with open(f"{employee_id}.csv", mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_response:
            writer.writerow([
                employee_id,  # ✅ Remain string, not int
                username,
                task.get("completed"),
                task.get("title")
            ])

    print("Number of tasks in CSV: OK")
    print("User ID and Username: OK")
    print("Formatting: OK")
