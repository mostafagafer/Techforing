
import requests

# Base URL of your API
BASE_URL = 'http://127.0.0.1:8000/api/'

# Token from the login response
TOKEN = '52ba8bf8683326c0a99bf1e62bd1c6c513c6588b'

# Test Deleting a Project
def test_delete_project(project_id):
    url = BASE_URL + f'projects/{project_id}/'  # URL for the specific project
    headers = {
        'Authorization': f'Token {TOKEN}'  # Include the token in the headers
    }
    response = requests.delete(url, headers=headers)  # Send a DELETE request
    
    print("Testing Project Deletion:")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 204:
        print("Project deleted successfully!")
    else:
        print("Failed to delete project.")

# Main function to run the test
def main():
    project_id = 5  # The ID of the project you want to delete
    test_delete_project(project_id)

if __name__ == "__main__":
    main()


