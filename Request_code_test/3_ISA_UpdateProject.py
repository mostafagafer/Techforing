import requests

# Base URL of your API
BASE_URL = 'http://127.0.0.1:8000/api/'

# Token from the login response
TOKEN = '52ba8bf8683326c0a99bf1e62bd1c6c513c6588b'

# Test Updating a Project
def test_update_project(project_id):
    url = BASE_URL + f'projects/{project_id}/'  # URL for the specific project
    headers = {
        'Authorization': f'Token {TOKEN}'  # Include the token in the headers
    }
    data = {
        'name': 'My First Project',  # Keep the same name
        'description': 'This is a test project created using the API.',  # Keep the same description
        'members': [
            {'user': 3, 'role': 'Member'},  # Add User 3 as a Member
            {'user': 4, 'role': 'Member'},  # Add User 4 as a Member
        ]
    }
    response = requests.put(url, json=data, headers=headers)  # Use PUT to update the project
    
    print("Testing Project Update:")
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

    if response.status_code == 200:
        print("Project updated successfully!")
    else:
        print("Failed to update project.")

# Main function to run the test
def main():
    project_id = 4  # The ID of the project you want to update
    test_update_project(project_id)

if __name__ == "__main__":
    main()