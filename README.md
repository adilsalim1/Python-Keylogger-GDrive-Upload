Python Keylogger with Google Drive Upload

Overview

This Python script serves as a secure keylogger with Google Drive integration. It captures keyboard inputs and securely uploads them to a specified Google Drive folder. The project uses the pynput library for keystroke monitoring and the Google Drive API for encrypted log storage.
Features

    Google Drive Integration: Logs are automatically uploaded to a specified Google Drive folder.
    Simple Setup: Easy installation and configuration for quick deployment.
    Educational Purpose: Ideal for learning about keylogger functionality and API integration.
    Privacy Considerations: Use responsibly and be aware of potential legal implications.

Installation

1. Clone the repository:

   git clone https://github.com/YourUsername/Python-Keylogger-GDrive-Upload.git
   cd Python-Keylogger-GDrive-Upload

3. Install required libraries:
   
   pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib pynput

4. Set up the Google Drive API:

    Create a project on the Google Cloud Console.
    Enable the Google Drive API.
    Create a service account and download the JSON key file.
    Share the target Google Drive folder with the service account email.

5.  Configure the script:
    pen keylogger.py and replace SERVICE_ACCOUNT_FILE and PARENT_FOLDER_ID with your values.

