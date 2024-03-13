# prodigyTask4_cyberSecurity-keylogger

Below is the documentation for the provided keylogger script, explaining its purpose, functionalities, and usage.

Keylogger Documentation
Overview
The keylogger is a Python script that captures and logs keystrokes from the user's keyboard input. It utilizes the pynput library to monitor keyboard events and the tkinter library to create a simple Graphical User Interface (GUI) for starting, stopping, and exiting the keylogger application.

Features
Start Keylogger: Begins capturing keyboard input and logs it to a file named "keylog.txt".
Stop Keylogger: Halts the keylogging process.
Exit Application: Closes the GUI window and terminates the keylogger.
Requirements
Python 3.x
pynput library (pip install pynput)
Usage
Installation: Ensure Python 3.x is installed on your system. Install the pynput library using pip if it's not already installed: pip install pynput.

Running the Script: Execute the script using Python. This will open a GUI window with buttons to control the keylogger.

Starting the Keylogger: Click on the "Start Keylogger" button to initiate the keylogging process. A confirmation message will appear, indicating that keystrokes are being logged to "keylog.txt".

Stopping the Keylogger: To stop the keylogger, click on the "Stop Keylogger" button. Another message will confirm that the keylogger has been stopped.

Exiting the Application: Click on the "Exit" button to close the GUI window and terminate the keylogger application.

File Output
The keylogger logs keystrokes to a file named "keylog.txt" in the current working directory. Each line in the log file represents a single keystroke event, including the timestamp and the key pressed.

Error Handling
The script includes error handling to capture and display any exceptions that may occur during the execution. If an error occurs while starting the keylogger, an error message will be shown to the user.

Security and Privacy
It's important to use this keylogger script responsibly and ethically. Keylogging without proper authorization may violate privacy laws and regulations. Always ensure that you have appropriate consent before using keylogging software.

Disclaimer
This keylogger script is provided for educational and learning purposes only. The authors do not endorse any illegal or unethical use of this software. Users are solely responsible for their actions when using this script.
