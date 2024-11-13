import tkinter as tk
from tkinter import messagebox
import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to handle the user's choice and display the result
def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    # Display the choices and result in the result label
    result_label.config(text=f"Computer chose: {computer_choice.capitalize()}\n{result}")
    
# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x400")

# Create a label for instructions
instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 16))
instruction_label.pack(pady=20)

# Create buttons for user choices
rock_button = tk.Button(root, text="Rock", width=20, height=2, font=("Arial", 14), command=lambda: play_game("rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=20, height=2, font=("Arial", 14), command=lambda: play_game("paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=20, height=2, font=("Arial", 14), command=lambda: play_game("scissors"))
scissors_button.pack(pady=5)

# Create a label for displaying the result
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Start the main event loop
root.mainloop()