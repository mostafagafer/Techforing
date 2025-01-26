import requests
from datetime import datetime, timedelta

# Base URL of your API
BASE_URL = 'http://127.0.0.1:8000/api/'

# Token from the login response
TOKEN = '52ba8bf8683326c0a99bf1e62bd1c6c513c6588b'

# Test Creating a Task
def test_create_task():
    url = BASE_URL + 'tasks/'  # URL for the tasks endpoint
    headers = {
        'Authorization': f'Token {TOKEN}'  # Include the token in the headers
    }
    # Set the due date to 7 days from now
    due_date = (datetime.now() + timedelta(days=7)).isoformat()

    data = {
        'title': 'Complete API Integration',
        'description': 'Integrate the REST API with the frontend application.',
        'status': 'To Do',  # Default status
        'priority': 'High',  # Priority of the task
        'assigned_to': 3,  # Assign the task to User 3
        'project': 4,  # Associate the task with Project 4
        'due_date': due_date  # Due date in ISO 8601 format
    }
    response = requests.post(url, json=data, headers=headers)  # Send a POST request
    
    print("Testing Task Creation:")
    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    print(f"Response Content: {response.text}")  # Print raw response content

    try:
        response_json = response.json()
        print(f"Response JSON: {response_json}")
    except ValueError as e:
        print(f"Failed to decode JSON: {e}")

    if response.status_code == 201:
        print("Task created successfully!")
        return response.json()['id']  # Return the task ID for future use
    else:
        print("Failed to create task.")
        return None

# Main function to run the test
def main():
    task_id = test_create_task()
    if task_id:
        print("Task ID:", task_id)

if __name__ == "__main__":
    main()