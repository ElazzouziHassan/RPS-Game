import tkinter as tk
from tkinter import ttk
import random

def determine_winner(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    if player_choice == computer_choice:
        result_label.config(text=f"Tie! You both chose {player_choice}.")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text=f"You win! {player_choice} beats {computer_choice}.")
    else:
        result_label.config(text=f"Computer wins! {computer_choice} beats {player_choice}.")

def player_choice(choice):
    determine_winner(choice)

window = tk.Tk()
window.title("Rock, Paper, Scissors Game")
window.geometry("400x300")

style = ttk.Style()
style.configure("TButton", padding=(10, 5, 10, 5), font=("Helvetica", 12))

rock_button = ttk.Button(window, text="Rock", command=lambda: player_choice("Rock"))
paper_button = ttk.Button(window, text="Paper", command=lambda: player_choice("Paper"))
scissors_button = ttk.Button(window, text="Scissors", command=lambda: player_choice("Scissors"))

rock_button.place(x=50, y=50)
paper_button.place(x=150, y=50)
scissors_button.place(x=250, y=50)

result_label = tk.Label(window, text="", font=("Helvetica", 14))
result_label.place(x=50, y=150)

window.mainloop()
