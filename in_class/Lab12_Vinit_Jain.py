# Author: Vinit Kirit Jain
# Assignment: Lab 12

# importing the necessary libraries
from PIL import Image, ImageTk
import os
import tkinter as tk

image_files = []
# creating a list of images to be displayed
for i in os.listdir():
    if i.endswith(".jpeg"):
        image_files.append(i)
print(image_files)

# creating a global variable to keep track of current image index
current_image_index = 0

# creating the initial window
main_window = tk.Tk()

# creating canvas for the first i.e. initial frame
initial_canvas = tk.Canvas(main_window, width=300, height=200)
initial_canvas.create_text(150, 100, text="Welcome!!")
initial_canvas.pack()

# creating next button
next_button = tk.Button(main_window, text="Next", command=lambda: open_next_window())
next_button.pack()


# define a function to load image
def load_image(image_file):
    image = Image.open(image_file)
    width, height = image.size
    ratio = min(300 / width, 200 / height)
    image = image.resize((int(width * ratio), int(height * ratio)))
    photo = ImageTk.PhotoImage(image)
    return photo


# define a function to update image on the canvas
def update_image():
    global current_image_index
    loaded_photo = load_image(image_files[current_image_index])
    initial_canvas.delete("all")
    initial_canvas.create_image(150, 100, image=loaded_photo)
    initial_canvas.image = loaded_photo


# define a function to display the next image
def show_next_image():
    global current_image_index
    current_image_index = (current_image_index + 1) % len(image_files)
    update_image()


# define a function to display the previous image
def show_previous_image():
    global current_image_index
    current_image_index = (current_image_index - 1) % len(image_files)
    update_image()


# define a function to close the new window and return to the main window
def close_window():
    image_window.destroy()


# define a function to create the new image window
def open_next_window():
    global current_image_index
    global image_window
    image_window = tk.Toplevel(main_window)
    image_window.title("Happy Thanksgiving!!")
    image_canvas = tk.Canvas(image_window, width=300, height=200)
    image_canvas.create_text(150, 100, text="Welcome!!")
    image_canvas.pack()

    # creating next button to view next image
    next_image_button = tk.Button(image_window, text="Next", command=show_next_image)
    next_image_button.pack()

    # creating previous button to view previous image
    previous_image_button = tk.Button(
        image_window, text="Previous", command=show_previous_image
    )
    previous_image_button.pack()

    # creating done button to return to the initial window
    done_button = tk.Button(image_window, text="Close", command=close_window)
    done_button.pack()

    # calling the update_image() function to display the first image
    update_image()


main_window.mainloop()
