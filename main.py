import requests

def getCred():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    credentials = {} 
    credentials['username'] = username
    credentials['password'] = password

    return credentials

def sendingRequest(credentials):
    response = requests.post("https://banweb.lau.edu.lb/pkmslogin.form" , data=credentials)
    return response.text


credentials = getCred()
print(sendingRequest(credentials))
