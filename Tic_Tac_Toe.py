import tkinter.messagebox
from tkinter import *


root=Tk()
root.title("Advanced Tic Tac Toe Game")
root.geometry("1155x750")
root.configure(bg="dodger blue")
root.resizable(width=FALSE,height=FALSE)

tops = Frame(root, bg="lavender", pady=2, width=1350, height=100, relief=RIDGE)
tops.place(x=0,y=0)

lblTitle = Label(tops, font=("ariel",45,"bold"), text="Advanced Tic Tac Toe Game", bd=5, bg="lavender",fg="gray11",justify=CENTER)
lblTitle.place(x=150,y=7)

mainFrame = Frame(root, bg="dodger blue", pady=2, width=1274, height=550, relief=RIDGE)
mainFrame.place(x=5,y=120)

leftFrame = Frame(mainFrame, bd=10, width=620, height=600, pady=2, padx=10, bg="slate grey", relief=RIDGE)
leftFrame.pack(side=LEFT)

rightFrame1 = Frame(mainFrame, bd=10, width=526, height=500, pady=2, padx=10, bg="MistyRose2", relief=RIDGE)
rightFrame1.pack(side=RIGHT)

rightFrame2 = Frame(mainFrame, bd=10, width=500, height=210, pady=2, padx=10, bg="dodger blue", relief=RIDGE)
rightFrame2.place(x=633,y=90)

rightFrame3 = Frame(mainFrame, bd=10, width=500, height=210, pady=2, padx=10, bg="dodger blue", relief=RIDGE)
rightFrame3.place(x=633,y=300)

PlayerX=IntVar()
PlayerO=IntVar()

PlayerX.set(0)
PlayerO.set(0)

buttons = StringVar()
click = True
gameDraw = False

def Checker(buttons):
    global gameDraw
    global click
    
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        CheckWin()    
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        CheckWin()

def CheckWin():
            
    if (button_1 ["text"] == "X" and button_2 ["text"] == "X" and button_3 ["text"] == "X" and button_1 ["text"] != " "):
        button_1.configure(bg="green yellow")
        button_2.configure(bg="green yellow")
        button_3.configure(bg="green yellow")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Player 1 won", "You have just won the game")
    elif (button_4 ["text"] == "X" and button_5 ["text"] == "X" and button_6 ["text"] == "X" and button_4 ["text"] != " "):
        button_4.configure(bg="green yellow")
        button_5.configure(bg="green yellow")
        button_6.configure(bg="green yellow")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Player 1 won", "You have just won the game")
    elif (button_7 ["text"] == "X" and button_8 ["text"] == "X" and button_9 ["text"] == "X" and button_7 ["text"] != " "):
        button_7.configure(bg="green yellow")
        button_8.configure(bg="green yellow")
        button_9.configure(bg="green yellow")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Player 1 won", "You have just won the game")
    elif (button_1 ["text"] == "X" and button_5 ["text"] == "X" and button_9 ["text"] == "X" and button_1 ["text"] != " "):
        button_1.configure(bg="green yellow")
        button_5.configure(bg="green yellow")
        button_9.configure(bg="green yellow")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Player 1 won", "You have just won the game")
    elif (button_3 ["text"] == "X" and button_5 ["text"] == "X" and button_7 ["text"] == "X" and button_3 ["text"] != " "):
        button_3.configure(bg="green yellow")
        button_5.configure(bg="green yellow")
        button_7.configure(bg="green yellow")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Player 1 won", "You have just won the game")
    elif (button_1 ["text"] == "X" and button_4 ["text"] == "X" and button_7 ["text"] == "X" and button_1 ["text"] != " "):
        button_1.configure(bg="green yellow")
        button_4.configure(bg="green yellow")
        button_7.configure(bg="green yellow")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Player 1 won", "You have just won the game")
    elif (button_2 ["text"] == "X" and button_5 ["text"] == "X" and button_8 ["text"] == "X" and button_2 ["text"] != " "):
        button_2.configure(bg="green yellow")
        button_5.configure(bg="green yellow")
        button_8.configure(bg="green yellow")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Player 1 won", "You have just won the game")
    elif (button_3 ["text"] == "X" and button_6 ["text"] == "X" and button_9 ["text"] == "X" and button_2 ["text"] != " "):
        button_3.configure(bg="green yellow")
        button_6.configure(bg="green yellow")
        button_9.configure(bg="green yellow")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Player 1 won", "You have just won the game")

    elif (button_1 ["text"] == "O" and button_2 ["text"] == "O" and button_3 ["text"] == "O" and button_1 ["text"] != " "):
        button_1.configure(bg="turquoise1")
        button_2.configure(bg="turquoise1")
        button_3.configure(bg="turquoise1")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Player 2 won", "You have just won the game")
    elif (button_4 ["text"] == "O" and button_5 ["text"] == "O" and button_6 ["text"] == "O" and button_4 ["text"] != " "):
        button_4.configure(bg="turquoise1")
        button_5.configure(bg="turquoise1")
        button_6.configure(bg="turquoise1")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Player 2 won", "You have just won the game")
    elif (button_7 ["text"] == "O" and button_8 ["text"] == "O" and button_9 ["text"] == "O" and button_7 ["text"] != " "):
        button_7.configure(bg="turquoise1")
        button_8.configure(bg="turquoise1")
        button_9.configure(bg="turquoise1")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Player 2 won", "You have just won the game")
    elif (button_1 ["text"] == "O" and button_5 ["text"] == "O" and button_9 ["text"] == "O" and button_1 ["text"] != " "):
        button_1.configure(bg="turquoise1")
        button_5.configure(bg="turquoise1")
        button_9.configure(bg="turquoise1")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Player 2 won", "You have just won the game")
    elif (button_3 ["text"] == "O" and button_5 ["text"] == "O" and button_7 ["text"] == "O" and button_3 ["text"] != " "):
        button_3.configure(bg="turquoise1")
        button_5.configure(bg="turquoise1")
        button_7.configure(bg="turquoise1")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Player 2 won", "You have just won the game")
    elif (button_1 ["text"] == "O" and button_4 ["text"] == "O" and button_7 ["text"] == "O" and button_1 ["text"] != " "):
        button_1.configure(bg="turquoise1")
        button_4.configure(bg="turquoise1")
        button_7.configure(bg="turquoise1")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Player 2 won", "You have just won the game")
    elif (button_2 ["text"] == "O" and button_5 ["text"] == "O" and button_8 ["text"] == "O" and button_2 ["text"] != " "):
        button_2.configure(bg="turquoise1")
        button_5.configure(bg="turquoise1")
        button_8.configure(bg="turquoise1")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Player 2 won", "You have just won the game")
    elif (button_3 ["text"] == "O" and button_6 ["text"] == "O" and button_9 ["text"] == "O" and button_3 ["text"] != " "):
        button_3.configure(bg="turquoise1")
        button_6.configure(bg="turquoise1")
        button_9.configure(bg="turquoise1")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Player 2 won", "You have just won the game")
    elif (button_1 ["text"] != " " and button_2 ["text"] != " " and button_3 ["text"] != " " and button_4 ["text"] != " " and button_5 ["text"] != " " and button_6 ["text"] != " " and button_7 ["text"] != " " and button_8 ["text"] != " " and button_9 ["text"] != " "):
        return draw()

def draw():
    gameDraw = True
    button_1.configure(bg="red")
    button_2.configure(bg="red")
    button_3.configure(bg="red")
    button_4.configure(bg="red")
    button_5.configure(bg="red")
    button_6.configure(bg="red")
    button_7.configure(bg="red")
    button_8.configure(bg="red")
    button_9.configure(bg="red")
    tkinter.messagebox.showinfo("Draw","Game is draw")
    reset()
              
def reset():
    button_1["text"]=" "
    button_2["text"]=" "
    button_3["text"]=" "
    button_4["text"]=" "
    button_5["text"]=" "
    button_6["text"]=" "
    button_7["text"]=" "
    button_8["text"]=" "
    button_9["text"]=" "
    
    button_1.configure(bg="white")
    button_2.configure(bg="white")
    button_3.configure(bg="white")
    button_4.configure(bg="white")
    button_5.configure(bg="white")
    button_6.configure(bg="white")
    button_7.configure(bg="white")
    button_8.configure(bg="white")
    button_9.configure(bg="white")
         
def newGame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)

lblPlayerX = Label(rightFrame2, font=("ariel", 40,"bold"), text="Player 1 :", padx=2, pady=2, bg="seashell2")
lblPlayerX.place(x=5,y=7)
lblPlayerX = Entry(rightFrame2, font=("ariel",40,"bold"), bd=2, fg="black", textvariable=PlayerX, width=7, justify=LEFT).place(x=255,y=7)

lblPlayerO = Label(rightFrame2, font=("ariel", 40,"bold"), text="Player 2 :", padx=2, pady=2, bg="seashell2")
lblPlayerO.place(x=5,y=110)
lblPlayerO = Entry(rightFrame2, font=("ariel",40,"bold"), bd=2, fg="black", textvariable=PlayerO, width=7, justify=LEFT).place(x=255,y=110)

buttonReset = Button(rightFrame3, text="Reset", font=("Times new roman",24,"bold"), height=1, width=22, pady=9, padx=8, bg="white",activebackground="tan1", command=reset)
buttonReset.place(x=8,y=7)

buttonNewGame = Button(rightFrame3, text="New Game", font=("Times new roman",24,"bold"), height=1, width=22, pady=9, padx=8, bg="white",activebackground="tan1", command=newGame)
buttonNewGame.place(x=8,y=100)

button_1 = Button(leftFrame, text=" ", font=("ariel",23,"bold"), height=4, width=9, pady=9, padx=8, bg="white", command=lambda:Checker(button_1))
button_1.place(x=-3,y=8)

button_2 = Button(leftFrame, text=" ", font=("ariel",23,"bold"), height=4, width=9, pady=9, padx=8, bg="white", command=lambda:Checker(button_2))
button_2.place(x=193,y=8)

button_3 = Button(leftFrame, text=" ", font=("ariel",23,"bold"), height=4, width=9, pady=9, padx=8, bg="white", command=lambda:Checker(button_3))
button_3.place(x=389,y=8)

button_4 = Button(leftFrame, text=" ", font=("ariel",23,"bold"), height=4, width=9, pady=9, padx=8, bg="white", command=lambda:Checker(button_4))
button_4.place(x=-3,y=197)

button_5 = Button(leftFrame, text=" ", font=("ariel",23,"bold"), height=4, width=9, pady=9, padx=8, bg="white", command=lambda:Checker(button_5))
button_5.place(x=193,y=197)

button_6 = Button(leftFrame, text=" ", font=("ariel",23,"bold"), height=4, width=9, pady=9, padx=8, bg="white", command=lambda:Checker(button_6))
button_6.place(x=389,y=197)

button_7 = Button(leftFrame, text=" ", font=("ariel",23,"bold"), height=4, width=9, pady=7, padx=8, bg="white", command=lambda:Checker(button_7))
button_7.place(x=-3,y=386)

button_8 = Button(leftFrame, text=" ", font=("ariel",23,"bold"), height=4, width=9, pady=7, padx=8, bg="white", command=lambda:Checker(button_8))
button_8.place(x=193,y=386)

button_9 = Button(leftFrame, text=" ", font=("arieln",23,"bold"), height=4, width=9, pady=7, padx=8, bg="white", command=lambda:Checker(button_9))
button_9.place(x=389,y=386)

root.mainloop()
