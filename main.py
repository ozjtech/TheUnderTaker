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

#the user will be able to create new sheets for new lists

#testing here



# #because of this we are naming sheet1 primary sheet, so that its special

primarySheet = client.open('underTakerDB').sheet1 


#building the menu
menu = ConsoleMenu("TheUnderTaker", "task organizer")

#FUNCTIONALITY FOR THE MENU ITEMS GOES UNDER THIS LINE

#creates a new spreadsheet
def newList():
    newSheetName = input("What would you like to call this list?")
    client.open('underTakerDB').add_worksheet(newSheetName, 400,400)
    newSheetConfirmation = "Your new tasklist %s is ready."
    print(newSheetConfirmation % newSheetName)



#add a task
def newTask():
    class task:
        def __init__(self):
            self.value = input("What would you like to accomplish? ")
            self.priority = input("What is the priority of this task? least, low or high? ")
        createTask = task()
#recursive task generator???
index = 2
#topPriority = str
#lowPriority = str
#leastPriority = str


#uses task.value to sort a given task and assign it to a place in the spreadsheet
def addTask(task):
    if (task.priority == 'high'):
        primarySheet.insert_row(task.value, index)
    if (task.priority == 'low'):
        primarySheet.insert_row(task.value, index)
    if (task.priority == 'least'):
        primarySheet.insert_row(task.value, index)
        #,lowPriority,leastPriority]
    #primarySheet.insert_row(row(), index)

#shows all sheets inside of the spreadsheet
def showAllLists():
    fetch = client.open('undertakerDB')
    for sheet in fetch:
        print(sheet)

#showAllLists() doesn't work yet

def startMenu():
#NEW MENU ITEMS GO UNDER THIS LINE AFTER THEIR FUNCTIONALITY

#create a submenu to show all sheets and let the user pick which one to print
    viewTasksOption = FunctionItem("View all task lists", showAllLists)
#create logic for adding tasks
#this DOESN"T WORK!?!?!?!
    addTaskOption = FunctionItem("Add a task", addTask(newTask))
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

startMenu()
