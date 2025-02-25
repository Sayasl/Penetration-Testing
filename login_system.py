import time
from flask import Flask, request, jsonify

users_db = {
    "user": "protect123",
    "admin": "admin12",
    "guest": "welcome"
}

app = Flask(__name__)

def authenticate(username, password):
    time.sleep(1)
    if username in users_db and users_db[username] == password:
            return True
    return False

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if authenticate(username, password):
        return "Login Successful", 200
    else:
        return "Invalid Credentials", 401
    
if __name__ == "__main__":
    # print("welcome to the login system")
    # username = input("Enter username:")
    # password = input("Enter password:")

    # print(login(username, password))
    app.run(host="127.0.0.2", port=4000)