# importing the requied packages
import tkinter as tk
from tkinter import messagebox
import random
# players stats and All  possibilities
player1 = "X"
player2 = "O" 
ALL_POSSIBILITIES = [
    # Rows  possibilities
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    # Columns  possibilities
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    # Diagonals  possibilities
    [0, 4, 8],
    [2, 4, 6]
]

# Initialize the board
gameboard = [" "] * 9

# Initialize the GUI
root = tk.Tk()
root.title("Tic-Tac-Toe Game")

# Create the buttons
buttons = []
for game in range(9):
    button = tk.Button(root, text=" ", width=40, height=20, command=lambda index=game: button_click(index))
    button.grid(row=game // 3, column=game % 3)
    buttons.append(button)

# Function to handle button clicks
def button_click(index):
    if gameboard[index] == " ":
        # Update the board and GUI
        gameboard[index] = player1
        buttons[index].config(text=player1)
        buttons[index].config(state=tk.DISABLED)
        # Check for a win or tie
        if check_win(player1):
            stop_game("player1 wins!")
        elif check_full_board():
            stop_game("It's a tie!")
        else:
            # Let the AI make a move
            ai_move()

# Function to let the AI make a move
def ai_move():
    # Check for available moves
    available_moves = []
    for game in range(9):
        if gameboard[game] == " ":
            available_moves.append(game)
    if len(available_moves) > 0:
        # Make a random move
        game = random.choice(available_moves)
        gameboard[game] = player2
        buttons[game].config(text=player2)
        buttons[game].config(state=tk.DISABLED)
        if check_win(player2):
            stop_game("player2 wins!")

# Function to check for a win
def check_win(player):
    for combination in ALL_POSSIBILITIES:
        if all(gameboard[i] == player for i in combination):
            return True
    return False

# Function to check if the board is full
def check_full_board():
    return all(cell != " " for cell in gameboard)

# Function to end the game
def stop_game(message):
    messagebox.showinfo("Result", message)
    root.quit()

# Start the GUI event loop
root.mainloop()
