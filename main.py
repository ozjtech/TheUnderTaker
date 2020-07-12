
#import dependencies [X]
#intergrate google sheets and drive APIS[]
#build menu[]
import random
import json
import pprint
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("mysteryBox.json", scope)
client = gspread.authorize(creds)

#the user will be able to create new sheets for new lists
# #because of this we are naming sheet1 primary sheet, so that its special
primarySheet = client.open('underTakerDB').sheet1
#simple pointer for our user to choose from
choice = []
#this function will act as our 'engine' that runs the problem until the user selects the 'exit' option in our menu
def undertaking():
    if(choice == 'end program'):
        exit