# Name: Vinit Jain
# Date: 2023-11-15
# Assignment: Lab 11
# Class: CPS 501

import tkinter as tk
from tkinter import filedialog

# setting up the main window
file_path = None


# defining a function to open a file dialog
def open_file():
    global file_path
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text files", ".txt"), ("All files", ".*")],
    )

    if file_path:
        print(f"file opened: {file_path}")


# defining a function to write to the file
def write_to_file():
    global file_path
    if not file_path:
        print("please open a file first.")
        return

    text_to_write = entry.get()

    if text_to_write:
        with open(file_path, "a") as file:
            file.write(text_to_write + "\n")
            print(f"text written to file: {text_to_write}")


# defining a function to handle entry modification
def on_entry_modified(event):
    print("entry modified:", entry.get())


# create the main window
root = tk.Tk()
root.title("text file writer")

# entry box
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# bind the modified event to the entry box
entry.bind("<<Modified>>", on_entry_modified)

# open button
open_button = tk.Button(root, text="open", command=open_file)
open_button.pack(pady=5)

# write button
write_button = tk.Button(root, text="write", command=write_to_file)
write_button.pack(pady=10)

# start the tkinter event loop
root.mainloop()
