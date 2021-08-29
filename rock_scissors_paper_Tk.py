from tkinter import*
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

window = Tk()
window.title("Rock, paper, scissors")
window.geometry("600x400")
window.resizable(width=False, height=False)
window["bg"] = "gray"

labelText = Label(window,
                  text="Choose: rock, scissors or paper",
                  fg="black",
                  font=("Times New Roman", 20),
                  bg="gray")
labelText.place(x=140, y=30)

rock_but = Button(window,
              text="Rock",
              font=("Comic Sans Ms", 25),
              bg="gray",
              command=rock)
rock_but.place(x=40, y=200)

cut_but = Button(window,
                 text="Scissors",
                 font=("Comic Sans Ms", 25),
                 bg="gray",
                 command=cut)
cut_but.place(x=200, y=200)

paper_but = Button(window,
                   text="Paper",
                   font=("Comic Sans Ms", 25),
                   bg="gray",
                   command=paper)
paper_but.place(x=430, y=200)

window.mainloop()
