#work in progess
#Right now you have to click on your letter after you get 3 in a row to check win

#importing tkinter
from tkinter import *
from tkinter import messagebox


tk = Tk()
tk.title("TIC TAC TOE")

click = True

#establishing clicks
def tictactoe(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True

# X win conditions
    elif(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
        button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
        button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
        button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
        button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
        button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
        button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        messagebox.showinfo("Player 1", "X's has won the game")

# O win conditions
    elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
        button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
        button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
        button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
        button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
        button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
        button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
        button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        messagebox.showinfo("Player 2", "O's has won the game")

#reset the game
def reset_game():
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "
    
#creating buttons
#adding buttons onto gid
buttons = StringVar()

button1 = Button(tk, text = " ",font = ('Arial 30 bold'), height = 5, width = 8, command = lambda:tictactoe(button1))
button1.grid(row = 1, column = 0, sticky = S+N+E+W)

button2 = Button(tk, text = " ",font = ('Arial 30 bold'), height = 5, width = 8, command = lambda:tictactoe(button2))
button2.grid(row = 1, column = 1, sticky = S+N+E+W)

button3 = Button(tk, text = " ",font = ('Arial 30 bold'), height = 5, width = 8, command = lambda:tictactoe(button3))
button3.grid(row = 1, column = 2, sticky = S+N+E+W)

button4 = Button(tk, text = " ",font = ('Arial 30 bold'), height = 5, width = 8, command = lambda:tictactoe(button4))
button4.grid(row = 2, column = 0, sticky = S+N+E+W)

button5 = Button(tk, text = " ",font = ('Arial 30 bold'), height = 5, width = 8, command = lambda:tictactoe(button5))
button5.grid(row = 2, column = 1, sticky = S+N+E+W)

button6 = Button(tk, text = " ",font = ('Arial 30 bold'), height = 5, width = 8, command = lambda:tictactoe(button6))
button6.grid(row = 2, column = 2, sticky = S+N+E+W)

button7 = Button(tk, text = " ",font = ('Arial 30 bold'), height = 5, width = 8, command = lambda:tictactoe(button7))
button7.grid(row = 3, column = 0, sticky = S+N+E+W)

button8 = Button(tk, text = " ",font = ('Arial 30 bold'), height = 5, width = 8, command = lambda:tictactoe(button8))
button8.grid(row = 3, column = 1, sticky = S+N+E+W)

button9 = Button(tk, text = " ",font = ('Arial 30 bold'), height = 5, width = 8, command = lambda:tictactoe(button9))
button9.grid(row = 3, column = 2, sticky = S+N+E+W)

button10 = Button(tk, text = "reset",font = ('Arial 30 bold'), height = 2, width = 8, command = reset_game)
button10.grid(row = 4, column = 1)

tk.mainloop()
