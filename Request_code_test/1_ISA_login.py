import requests

# Base URL of your API
BASE_URL = 'http://127.0.0.1:8000/api/'

# Test User Login
def test_login_user():
    url = BASE_URL + 'login/'
    data = {
        'username': 'testuser',
        'password': 'testpass123'
    }
    response = requests.post(url, json=data)
    
    print("Testing User Login:")
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    
    if response.status_code == 200:
        return response.json()['token']  # Return the token if login is successful
    else:
        return None

# Main function to run the test
def main():
    token = test_login_user()
    if token:
        print("Login successful! Token:", token)
    else:
        print("Login failed. Check your credentials or server logs.")

if __name__ == "__main__":
    main()


