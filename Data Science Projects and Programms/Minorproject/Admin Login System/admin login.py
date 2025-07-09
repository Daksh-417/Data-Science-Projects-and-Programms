import json
import os

LOGIN_FILE = "login_data.json"

def save_credentials(username, password):
    with open(LOGIN_FILE, "w") as f:
        json.dump({"username": username, "password": password}, f)

def load_credentials():
    # If login_data.json does not exist, create admin account
    if not os.path.exists(LOGIN_FILE):
        print("🔐 No admin account found. Let's create one.")
        username = input("Create admin username: ")
        password = input("Create admin password: ")
        save_credentials(username, password)
        print("✅ Admin account created successfully.\n")
    
    # Load credentials
    with open(LOGIN_FILE, "r") as f:
        data = json.load(f)
    return data["username"], data["password"]

def login():
    correct_user, correct_pass = load_credentials()
    attempts = 0

    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == correct_user and password == correct_pass:
            print("✅ Login Successful!")
            return True
        else:
            print("❌ Wrong username or password")
            attempts += 1

    print("🚫 Too many failed attempts. Access denied.")
    return False

# Run the login system
login()
