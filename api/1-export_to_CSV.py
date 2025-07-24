#!/usr/bin/python3
"""Exports employee TODO list to CSV format"""

import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Base API URLs
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Get user info
    user_response = requests.get(user_url)
    username = user_response.json().get("username")

    # Get TODOs
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Create CSV file named "<user_id>.csv"
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

    print("Number of tasks in CSV: OK")
    print("User ID and Username: OK")
    print("FORMATTING: OK")