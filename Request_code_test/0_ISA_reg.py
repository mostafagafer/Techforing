import requests

# Base URL of your API
BASE_URL = 'http://127.0.0.1:8000/api/'

# Test User Registration
def test_register_user():
    url = BASE_URL + 'register/'
    data = {
        'username': 'newuser',  # Replace with the desired username
        'email': 'newuser@example.com',  # Replace with the desired email
        'password': 'newpassword123',  # Replace with the desired password
        'first_name': 'New',  # Optional
        'last_name': 'User',  # Optional
    }
    response = requests.post(url, json=data)
    
    print("Testing User Registration:")
    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # Print raw response content

    try:
        response_json = response.json()
        print(f"Response JSON: {response_json}")
    except ValueError as e:
        print(f"Failed to decode JSON: {e}")

    if response.status_code == 201:
        print("User registered successfully!")
    else:
        print("Failed to register user.")

# Main function to run the test
def main():
    test_register_user()

if __name__ == "__main__":
    main()