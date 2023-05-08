import requests
from selenium import webdriver


def getCred():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    credentials = {} 
    credentials['username'] = username
    credentials['password'] = password

    return credentials

def sendingRequest(credentials):
    response = requests.post("https://banweb.lau.edu.lb/prod/pkmslogin.form" , data=credentials)
    return response.text

driver = webdriver.Chrome()
driver.get("https://banweb.lau.edu.lb/")


# credentials = getCred()
# print(sendingRequest(credentials))
