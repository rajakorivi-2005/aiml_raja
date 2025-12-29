try :
    username = input("Username: ")
    password = input("Password: ")

    if password != "admin123":
        raise ValueError("Incorrect password")
    
    print("Login successful")
except ValueError as e:
    print(e)
