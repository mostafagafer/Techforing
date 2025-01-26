import requests

# Base URL of your API
BASE_URL = 'http://127.0.0.1:8000/api/'

# Token from the login response
TOKEN = '52ba8bf8683326c0a99bf1e62bd1c6c513c6588b'

# Test Retrieving a Specific Project
def test_retrieve_project(project_id):
    url = BASE_URL + f'projects/{project_id}/'  # URL for the specific project
    headers = {
        'Authorization': f'Token {TOKEN}'  # Include the token in the headers
    }
    response = requests.get(url, headers=headers)  # Send a GET request
    
    print("Testing Project Retrieval:")
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

    if response.status_code == 200:
        print("Project retrieved successfully!")
    else:
        print("Failed to retrieve project.")

# Main function to run the test
def main():
    project_id = 4  # The ID of the project you want to retrieve
    test_retrieve_project(project_id)

if __name__ == "__main__":
    main()