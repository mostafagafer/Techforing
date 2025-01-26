
import requests

# Base URL of your API
BASE_URL = 'http://127.0.0.1:8000/api/'

# Token from the login response
TOKEN = '52ba8bf8683326c0a99bf1e62bd1c6c513c6588b'

# Test Listing Projects
def test_list_projects():
    url = BASE_URL + 'projects/'  # URL for the projects endpoint
    headers = {
        'Authorization': f'Token {TOKEN}'  # Include the token in the headers
    }
    response = requests.get(url, headers=headers)  # Send a GET request
    
    print("Testing Project List:")
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

    if response.status_code == 200:
        print("Projects fetched successfully!")
    else:
        print("Failed to fetch projects.")

# Main function to run the test
def main():
    test_list_projects()

if __name__ == "__main__":
    main()


