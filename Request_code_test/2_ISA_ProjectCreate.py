import requests

# Base URL of your API
BASE_URL = 'http://127.0.0.1:8000/api/'

# Token from the login response
TOKEN = '52ba8bf8683326c0a99bf1e62bd1c6c513c6588b'

# Test Creating a Project
def test_create_project():
    url = BASE_URL + 'projects/'
    headers = {
        'Authorization': f'Token {TOKEN}'  # Include the token in the headers
    }
    data = {
        'name': 'My 3rd Project ISA',
        'description': 'ISA This is a test project created using the API Update.',
    }
    response = requests.post(url, json=data, headers=headers)
    
    print("Testing Project Creation:")
    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    print(f"Response Content: {response.text}")  # Print raw response content

    try:
        response_json = response.json()
        print(f"Response JSON: {response_json}")
    except ValueError as e:
        print(f"Failed to decode JSON: {e}")

    if response.status_code == 201:
        print("Project created successfully!")
        return response.json()['id']  # Return the project ID for future use
    else:
        print("Failed to create project.")
        return None

# Main function to run the test
def main():
    project_id = test_create_project()
    if project_id:
        print("Project ID:", project_id)

if __name__ == "__main__":
    main()