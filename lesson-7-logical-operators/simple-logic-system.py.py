correct_username = "admin"
correct_password = "python123"

username = input("Enter your password:")
password = input("Enter your password:")

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid username or password")