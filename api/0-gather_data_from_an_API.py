#!/usr/bin/python3
"""Script to fetch employee TODO progress from JSONPlaceholder API"""

import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee details
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    employee_name = user_response.json().get("name")

    # Get employee's TODO list
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Count completed tasks
    completed_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    # Print required output
    print(f"Employee {employee_name} is done with tasks"
          f"({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
