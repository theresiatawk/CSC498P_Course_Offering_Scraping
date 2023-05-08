import requests
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
import time


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

# Creating new web driver to automatically fill the credentials
webDriver = webdriver.Chrome()
# Getting the banner login page into the driver
webDriver.get("https://banweb.lau.edu.lb/")
# Getting the login form's elements and filling them appropriatly 
loginField = webDriver.find_element(by="id", value="username")
loginField.send_keys("username")
passwordField = webDriver.find_element(by="id", value="password")
passwordField.send_keys("password")
loginButton = webDriver.find_element(by=By.CSS_SELECTOR, value='[type="submit"]')
loginButton.click()

# going to the menu where we can find the operations of the banner
menuLink = webDriver.find_element(by=By.CSS_SELECTOR , value="[title='Student Services and Financial Aid']")
menuLink.click()

## Going to the registration menu
registrationLink =  webDriver.find_element(by=By.LINK_TEXT , value="Registration")
registrationLink.click()

## Look-up Classes to Add menu
lookupLink = webDriver.find_element(by=By.LINK_TEXT, value="Look-up Classes to Add")
lookupLink.click()

## Going to the advanced search section
semester = Select(webDriver.find_element(by="id", value="term_input_id"))
semester.select_by_visible_text("Fall 2023 (View only)")
submitButton = webDriver.find_element(by=By.CSS_SELECTOR, value='[value="Submit"]')
submitButton.click()
advancedSearch = webDriver.find_element(by=By.CSS_SELECTOR, value='[value="Advanced Search"]')
advancedSearch.click()
time.sleep(15)


# credentials = getCred()
# print(sendingRequest(credentials))
