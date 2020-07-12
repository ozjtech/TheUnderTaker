
#import dependencies [X]
#intergrate google sheets and drive APIS[X]
#build menu[X]
#find out how to print a list of every sheet in the workspace[]
#maybe by creating a variable that has a for loop of sheet1 - ??? idk it just needs to work    
#create a function that generates a new submenu each time a new sheet is generated[]
#findout hwo to get rid of all these unused import errors.
import random
import json
import pprint
import datetime
from consolemenu import *
from consolemenu.items import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("mysteryBox.json", scope)
client = gspread.authorize(creds)

#the user will be able to create new sheets for new lists
# #because of this we are naming sheet1 primary sheet, so that its special
primarySheet = client.openall('underTakerDB')#.sheet1 

#building the menu
menu = ConsoleMenu("TheUnderTaker", "task organizer")


#FUNCTIONALITY FOR THE MENU ITEMS GOES UNDER THIS LINE

#creates a new spreadsheet
def newList():
    newSheetName = input("What would you like to call this list?")
    client.open('underTakerDB').add_worksheet(newSheetName, 400,400)
    newSheetConfirmation = "Your new tasklist %s is ready."
    print(newSheetConfirmation % newSheetName)

def showAllLists():
    everyList = primarySheet.sheet
    print(everyList)
#NEW MENU ITEMS GO UNDER THIS LINE AFTER THEIR FUNCTIONALITY

showAllLists()
def startMenu():
#create a submenu to show all sheets and let the user pick which one to print
    viewTasksOption = FunctionItem("View all task lists", showAllLists)
#create logic for adding tasks
    addTaskOption = MenuItem("Add a task")
#create logic for updating tasks
    updateATaskOption = MenuItem("Update a task")
#create logic for new tasks
    newTaskListOption = FunctionItem("New Task list", newList)
#create logic for deleting tasks
    deleteATaskOption = MenuItem("Delete a task")
#adding menu items to the menu
    menu.append_item(viewTasksOption)
    menu.append_item(addTaskOption)
    menu.append_item(updateATaskOption)
    menu.append_item(newTaskListOption)
    menu.append_item(deleteATaskOption)
#calling show to show the menu and allow the user to interact
    menu.show()
#commenting this out to test
#startMenu()

