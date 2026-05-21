import tkinter as tk
# this is for the graphics -> the board 
import random

# this is for the random generation of the food 

# basic constants
ROWS = 25
COLS = 25 
TILE_SIZE = 25

WINDOW_WIDTH = COLS * TILE_SIZE
WINDOW_HEIGHT = ROWS * TILE_SIZE

# creating the game window. 
window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

# creating a canvas for the game
canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
canvas.pack()

window.update_idletasks()

# center the window 
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = window.winfo_width()
window_height = window.winfo_height()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()




