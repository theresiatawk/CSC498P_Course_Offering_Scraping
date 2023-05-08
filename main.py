import requests
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as soup
import time
import csv


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


def getCourses(userCredentials):
    username = userCredentials['username']
    password = userCredentials['password']
# Creating new web driver to automatically fill the credentials
    webDriver = webdriver.Chrome()
    # Getting the banner login page into the driver
    webDriver.get("https://banweb.lau.edu.lb/")
    # Getting the login form's elements and filling them appropriatly 
    loginField = webDriver.find_element(by="id", value="username")
    loginField.send_keys(username)
    passwordField = webDriver.find_element(by="id", value="password")
    passwordField.send_keys(password)
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

    ## performing the search 
    major = Select(webDriver.find_element(by="id", value="subj_id"))
    major.select_by_visible_text("Computer Science")
    campus = Select(webDriver.find_element(by="id", value="camp_id"))
    campus.select_by_visible_text("Byblos")
    sectionSearch = webDriver.find_element(by=By.CSS_SELECTOR, value='[value="Section Search"]')
    sectionSearch.click()
    return webDriver.page_source


def coursesToCSV(pageSource):
    html = soup(pageSource , "html.parser")
    table = html.find("table", {"class": "datadisplaytable"})
    table_rows = list()
    for row in table.findAll("tr"):
        table_rows.append(row)
    with open("Courses.csv" , "w") as file:
        csvWrtiter = csv.writer(file)
        for i in range(1, len(table_rows)):
            cells = list()
            row = table_rows[i]
            if i != 1:
                for cell in row.findAll(["td", "th"]):
                    if row.findAll(["td", "th"]).index(cell) != 0 and row.findAll(["td", "th"]).index(
                            cell) < 20:
                        if cell.string:
                            cells.append(cell.string.strip())
                        else:
                            children = cell.findAll()
                            for i in children:
                                cells.append(i.string.strip())
                if len(cells) > 4:
                    if eval(cells[4]) != 1:
                        csvWrtiter.writerow(cells)
                else:
                    csvWrtiter.writerow(cells)
            else:
                for cell in row.findAll(["td", "th"]):
                    if row.findAll(["td", "th"]).index(cell) != 0 and row.findAll(["td", "th"]).index(
                            cell) < 20:
                        if cell.string:
                            cells.append(cell.string.strip())
                        else:
                            children = cell.findAll()
                            for i in children:
                                cells.append(i.string.strip())
                csvWrtiter.writerow(cells)


credentials = getCred()
courses = getCourses(credentials)
coursesToCSV(courses)