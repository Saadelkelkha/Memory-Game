from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Memory Game")

cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H']
random.shuffle(cards)

buttons = []
prev_card = None

def create_board():
    for i in range(4):
        for j in range(4):
            button = Button(root, text=" ", width=5, height=2, command=lambda row=i, col=j: flip_card(row, col))
            button.grid(row=i, column=j)
            buttons.append(button)

def flip_card(row, col):
    global prev_card
    index = row * 4 + col
    buttons[index].config(text=cards[index], state=DISABLED)

    if prev_card is None:
        prev_card = (index, cards[index])
    else:
        if prev_card[1] == cards[index]:
            messagebox.showinfo("Match", "You found a match!")
            buttons[prev_card[0]].config(state=DISABLED)
            buttons[index].config(state=DISABLED)
        else:
            messagebox.showinfo("No Match", "Try again.")
            buttons[prev_card[0]].config(text=" ", state=NORMAL)
            buttons[index].config(text=" ", state=NORMAL)

        prev_card = None

def reset_game():
    global cards, prev_card
    random.shuffle(cards)
    prev_card = None
    for button in buttons:
        button.config(text=" ", state=NORMAL)

create_board()

reset_button = Button(root, text="Reset", command=reset_game, font=("Arial", 16))
reset_button.grid(row=4, column=0, columnspan=2, pady=10)

exit_button = Button(root, text="Exit", font=("Arial", 16), command=lambda: exit())
exit_button.grid(row=4, column=2, columnspan=2, pady=10)

root.mainloop()