# Password Manager Readme🔏
## Overview
This is a simple password manager GUI application implemented in Python using the Tkinter library.    
The application allows users to generate random passwords, save website credentials (website, username/email, password), and search for saved credentials.   

## Features✨
* Password Generator: Generates a random password with a combination of letters (both uppercase and lowercase), numbers, and symbols.
* Save Password: Allows users to save website credentials, including the website name, username/email, and password.
* Search Account: Enables users to search for saved credentials by providing the website name.

## How to Use
### Generate Password:
* Click the "Generate Password" button to create a random password.   
* The generated password is displayed in the "Password" entry field.
* The password is **automatically copied** to the clipboard for easy use.
### Save Password:

* Enter the website name, username/email, and password in the respective entry fields.
* Click the "Add" button to save the credentials.
* A confirmation message will be displayed, and the entry fields will be cleared.
### Search Account:

* Enter the website name in the "Website" entry field.
* Click the "Search" button to find and display the saved credentials for that website.
* If the website is not found, a message indicating the absence of data will be displayed.
## UI Components
Labels, Entries, Buttons, Canvas

## Important Notes❗
* The application uses a JSON file (data.json) to store saved credentials. 
* If the JSON file does not exist, it will be created when the first set of credentials is saved.
## Dependencies
* Tkinter: for the graphical user interface.
* Pyperclip: for copying passwords to the clipboard.
* Random: for generating random passwords.
* JSON: for handling data storage in JSON format.
## How to Run
* Run the script in a Python environment.
*  Make sure you have the required libraries installed.

## Author
[Chaw Thiri San](chaw.compare)

