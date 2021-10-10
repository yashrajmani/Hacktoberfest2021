from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title("Die roll using Tkinter")
root.iconbitmap("./assets/python.ico")
root.geometry("700x450")

def rollEm():
    global imgList, dieLabel1, dieLabel2, dieLabel3, value, button, spin, dieNum1, dieNum2, dieNum3, msgLabel, score
    dieNum1 = random.choice(imgList)
    dieNum2 = random.choice(imgList)
    dieNum3 = random.choice(imgList)
    button.grid_forget()
    dieLabel1.grid_forget()
    dieLabel2.grid_forget()
    dieLabel3.grid_forget()
    msgLabel.grid_forget()
    spin.grid_forget()
    calcSum()
    if value.get() == 1:
        dieLabel1 = Label(root, image=dieNum1)
        dieLabel1.grid(row=2, column=0, pady=47)
        button = Button(root, text="Let's roll em", command=rollEm, bg="#5ebfff", fg="#fefefe", font=("poppins", 14))
        button.grid(row=0, column=0, columnspan=1, padx=285, pady=25)
        value = IntVar()
        spin = Spinbox(root, textvariable=value, from_=1, to=3)
        value.set(1)
        spin.grid(row=1, column=0, columnspan=1)
        msgLabel = Label(root, text=f"Great! You've got a sum of {score}", font=("poppins", 14))
        msgLabel.grid(row=3, column=0, columnspan=1)
    elif value.get() == 2:
        dieLabel1 = Label(root, image=dieNum1)
        dieLabel2 = Label(root, image=dieNum2)
        dieLabel1.grid(row=2, column=0, pady=47)
        dieLabel2.grid(row=2, column=1, pady=47)
        button = Button(root, text="Let's roll em", command=rollEm, bg="#5ebfff", fg="#fefefe", font=("poppins", 14))
        button.grid(row=0, column=0, columnspan=2, padx=285, pady=25)
        value = IntVar()
        spin = Spinbox(root, textvariable=value, from_=1, to=3)
        value.set(2)
        spin.grid(row=1, column=0, columnspan=2)
        msgLabel = Label(root, text=f"Great! You've got a sum of {score}", font=("poppins", 14))
        msgLabel.grid(row=3, column=0, columnspan=2)
    elif value.get() == 3:
        dieLabel1 = Label(root, image=dieNum1)
        dieLabel2 = Label(root, image=dieNum2)
        dieLabel3 = Label(root, image=dieNum3)
        dieLabel1.grid(row=2, column=0, pady=47)
        dieLabel2.grid(row=2, column=1, pady=47)
        dieLabel3.grid(row=2, column=2, pady=47)
        button = Button(root, text="Let's roll em", command=rollEm, bg="#5ebfff", fg="#fefefe", font=("poppins", 14))
        button.grid(row=0, column=0, columnspan=3, padx=285, pady=25)
        value = IntVar()
        spin = Spinbox(root, textvariable=value, from_=1, to=3)
        value.set(3)
        spin.grid(row=1, column=0, columnspan=3)
        msgLabel = Label(root, text=f"Great! You've got a sum of {score}", font=("poppins", 14))
        msgLabel.grid(row=3, column=0, columnspan=3)

def calcSum():
    global score, value, imgList, dieNum1, dieNum2, dieNum3, score
    if value.get() == 1:
        score = imgList.index(dieNum1) + 1
    elif value.get() == 2:
        score = imgList.index(dieNum1) + imgList.index(dieNum2) + 2
    elif value.get() == 3:
        score = imgList.index(dieNum1)+ imgList.index(dieNum2)+ imgList.index(dieNum3)+ 3

value = IntVar()
spin = Spinbox(root, textvariable=value, from_=1, to=3)
value.set(2)
spin.grid(row=1, column=0, columnspan=2)

button = Button(root, text="Let's roll em", command=rollEm, bg="#5ebfff", fg="#fefefe", font=("poppins", 14))
button.grid(row=0, column=0, columnspan=2, padx=285, pady=25)

dieImg1 = ImageTk.PhotoImage(Image.open("./assets/die1.png"))
dieImg2 = ImageTk.PhotoImage(Image.open("./assets/die2.png"))

dieImg3 = ImageTk.PhotoImage(Image.open("./assets/die3.png"))
dieImg4 = ImageTk.PhotoImage(Image.open("./assets/die4.png"))
dieImg5 = ImageTk.PhotoImage(Image.open("./assets/die5.png"))
dieImg6 = ImageTk.PhotoImage(Image.open("./assets/die6.png"))

msgLabel = Label(root, text="I dare you to roll the dice!!", font=("poppins", 14))
msgLabel.grid(row=3, column=0, columnspan=2)

imgList = [dieImg1, dieImg2, dieImg3, dieImg4, dieImg5, dieImg6]

dieLabel1 = Label(root, image=dieImg1)
dieLabel2 = Label(root, image=dieImg2)
dieLabel3 = Label(root, image=dieImg3)
dieLabel1.grid(row=2, column=0, pady=47)
dieLabel2.grid(row=2, column=1, pady=47)

root.mainloop()