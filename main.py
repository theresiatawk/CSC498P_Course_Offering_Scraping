

def getCred():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    credentials = {} 
    credentials['username'] = username
    credentials['password'] = password

    return credentials