# author: Vinit Kirit Jain
# date of creation: 2023-11-26

"""
description: A simple Rock, Paper, and Scissors game using tkinter.
"""

# importing the necessary modules
import random
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox


# defining main function
def main():
    # creating a new window
    window = tk.Tk()
    # defining the title of the window
    window.title("Rock, Paper, and Scissors Game")

    user_name = tk.simpledialog.askstring("User's Name", "Enter Your Name:")

    # initializing variable for radio buttons
    var = tk.StringVar()

    # importing the rock image
    rock_image = tk.PhotoImage(file="Picture1.png")

    # importing the paper image
    paper_image = tk.PhotoImage(file="Picture2.png")

    # importing the scissor image
    scissors_image = tk.PhotoImage(file="Picture3.png")

    # code to display the rock, paper, and scissor radio buttons with images
    rock_button = tk.Radiobutton(window, image=rock_image, variable=var, value="Rock")
    paper_button = tk.Radiobutton(
        window, image=paper_image, variable=var, value="Paper"
    )
    scissors_button = tk.Radiobutton(
        window, image=scissors_image, variable=var, value="Scissors"
    )

    submit_button = tk.Button(
        window, text="Submit", command=lambda: start_game(var.get(), user_name, window)
    )

    # aligning buttons to the center horizontally
    rock_button.pack(side="left", anchor="center")
    paper_button.pack(side="left", anchor="center")
    scissors_button.pack(side="left", anchor="center")
    submit_button.pack(side="left", anchor="center")

    # entering the tkinter event loop
    window.mainloop()


# defining a function to initiate the game
def start_game(player_choice, user_name, window):
    # calling get_random_choice() to get the value for the computer
    computer_choice = get_random_choice()

    # calling the check_for_winner() function to determine the winner based on the rules defined
    result = check_for_winner(player_choice, computer_choice, user_name)

    new_window = tk.Toplevel(window)
    new_window.title("New Window")

    # displaying the result in a messagebox
    label = tk.Label(
        new_window,
        text="Result Your choice: "
        + player_choice
        + " Computer's choice: "
        + computer_choice
        + " Result: "
        + result,
    )
    label.pack(padx=20, pady=20)

    # Add a button to close the new window
    close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=10)


# defining a function to select a random value from rock, paper, and scissor for the computer
def get_random_choice():
    # defining the list of choices
    choices = ["Rock", "Paper", "Scissors"]

    # selecting a random value from the list of available choices
    return random.choice(choices)


# defining a function to check the winner of the round by comparing the values selected by the user and computer
def check_for_winner(player_choice, computer_choice, user_name):
    # when the user and computer select the same values, it's a tie
    if player_choice == computer_choice:
        return "Tie!"

    # when the user is selecting rock and the computer is selecting scissors, then the user is winning
    elif player_choice == "Rock" and computer_choice == "Scissors":
        return user_name + " wins!"

    # when the user is selecting paper and the computer is selecting rock, then the user is winning
    elif player_choice == "Paper" and computer_choice == "Rock":
        return user_name + " wins!"

    # when the user is selecting scissors and the computer is selecting paper, then the user is winning
    elif player_choice == "Scissors" and computer_choice == "Paper":
        return user_name + " wins!"

    # otherwise, the computer is winning
    else:
        return "Computer has won!"


main()
