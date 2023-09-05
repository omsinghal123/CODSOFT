import random
from tkinter import *

def play_game(player_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "You lose!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

root = Tk()
root.title("GAME ")

rock_button = Button(root, text="Rock", padx=150, pady=25, command=lambda: play_game('rock'), bg="#D8BFD8")
rock_button.pack()

paper_button = Button(root, text="Paper", padx=150, pady=25, command=lambda: play_game('paper'), bg="#D8BFD8")
paper_button.pack()

scissors_button = Button(root, text="Scissors", padx=150, pady=25, command=lambda: play_game('scissors'), bg="#D8BFD8")
scissors_button.pack()

result_label = Label(root,   padx=150, pady=25,text="", font=("Arial", 20), bg="#D2B48C")
result_label.pack()

root.mainloop()