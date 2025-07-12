def login():
    attempts = 0

    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == correct_user and password == correct_pass:
            print("Login Successful!")
            break
        else:
            print("Wrong username or password")
            attempts += 1
        if attempts == 3:
            print("Too many attempts. Access denied.")
correct_user = "admin"
correct_pass = "1234"
login()
