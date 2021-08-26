import tkinter as tk
from tkinter import messagebox
from random import choice

def rock():
    game = ["r", "s", "p"]
    computer = choice(game)
    if computer == "p":
        messagebox.showinfo("Title", "You lose, bot chose 'paper'")
    elif computer == "s":
        messagebox.showinfo("Title", "Congratulations, you win. Bot chose 'scissors'")
    else:
        messagebox.showinfo("Title", "The draw game, bot also chose 'rock'")
def cut():
    game = ["r", "s", "p"]
    computer = choice(game)
    if computer == "r":
        messagebox.showinfo("Title", "You lose, bot chose 'rock'")
    elif computer == "p":
        messagebox.showinfo("Title", "Congratulations, you win. Bot chose 'paper'")
    else:
        messagebox.showinfo("Title", "The draw game, bot also chose 'scissors'")
def paper():
    game = ["r", "s", "p"]
    computer = choice(game)
    if computer == "s":
        messagebox.showinfo("Title", "You lose, bot chose 'scissors'")
    elif computer == "r":
        messagebox.showinfo("Title", "Congratulations, you win. Bot chose 'rock'")
    else:
        messagebox.showinfo("Title", "The draw game, bot also chose 'paper'")

window = tk.Tk()

window.rowconfigure(0, minsize=100, weight=1)
window.columnconfigure([0, 1, 2], minsize=100, weight=1)

btn_rock = tk.Button(master=window, text="Rock",
                     bg="gray", fg="white", relief=tk.RIDGE, command=rock)
btn_rock.grid(row=0, column=0, sticky="nsew")
btn_cut = tk.Button(master=window, text="Scissors",
                    bg="gray", fg="white", relief=tk.RIDGE, command=cut)
btn_cut.grid(row=0, column=1, sticky="nsew")
btn_paper = tk.Button(master=window, text="Paper",
                    bg="gray", fg="white", relief=tk.RIDGE, command=paper)
btn_paper.grid(row=0, column=2, sticky="nsew")

window.mainloop()