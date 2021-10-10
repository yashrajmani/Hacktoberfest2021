from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from dateutil import relativedelta

# creating the root/master widget
root = Tk()
root.title("Age Calculator using Tkinter")
root.iconbitmap("./assets/python.ico")
root.geometry("650x450")
root.configure(background="#ff793b")

# function for receiving values from entry widgets and assigning them to variables 
# also displays the final meassage label in the right format
def calcFn():
    global name, day, month, year, msgLabel
    name = nameEntry.get()
    day = int(dayEntry.get())
    month = int(monthEntry.get())
    year = int(yearEntry.get())
    ageFn()
    msgLabel.grid_forget()
    msgLabel = Label(root, text=f"Hey {name}, you are {ageFormat} old!!", font=("poppins",11), bg="#ff793b", fg="#dbfffe")
    msgLabel.grid(row=5, column=0, columnspan=4, pady=17)

# fuction for assigning the right string and date formats to the ageFormat variable used in previous function
# the formats depend upon the input value received from the option menu variable
def ageFn():
    global ageFormat, clicked
    dob = datetime(year=year, month=month, day=day)
    now = datetime.now()
    diff = now - dob
    diffRel = relativedelta.relativedelta(now, dob)
    totSec = int(diff.total_seconds())
    totHrs = int(totSec//3600)
    totDays = int(totHrs//24)
    totMon = (diffRel.years*12) + diffRel.months
    remDays = diffRel.days
    totYears = diffRel.years
    remMon = diffRel.months
    if clicked.get() == "In Years":
        ageFormat = f"{totYears} Years {remMon} Months {remDays} Days"
    elif clicked.get() == "In Months":
        ageFormat = f"{totMon} Months {remDays} Days"
    elif clicked.get() == "In Days":
        ageFormat = f"{totDays} Days"
    elif clicked.get() == "In Hours":
        ageFormat = f"{totHrs} Hours"
    elif clicked.get() == "In Seconds":
        ageFormat = f"{totSec} Seconds"

# the image to be displayed
myImg = ImageTk.PhotoImage(Image.open("./assets/age.png"))
imgLabel = Label(root, image=myImg, bg="#ff793b")
imgLabel.grid(row=0, column=0, pady=32, columnspan=4)

# the name label and entry widgets
nameLabel = Label(root, text="Name", font="Poppins", bg="#ff793b")
nameEntry = Entry(root, width=20, border=3)
nameLabel.grid(row=1, column=0, padx=17)
nameEntry.grid(row=2, column=0, padx=17)

# the day label and entry widgets
dayLabel = Label(root, text="Day", font="Poppins", bg="#ff793b")
dayEntry = Entry(root, width=20, border=3)
dayLabel.grid(row=1, column=1, padx=17)
dayEntry.grid(row=2, column=1, padx=17)

# the month label and entry widgets
monthLabel = Label(root, text="Month", font="Poppins", bg="#ff793b")
monthEntry = Entry(root, width=20, border=3)
monthLabel.grid(row=1, column=2, padx=17)
monthEntry.grid(row=2, column=2, padx=17)

# the year label and entry widgets
yearLabel = Label(root, text="Year", font="Poppins", bg="#ff793b")
yearEntry = Entry(root, width=20, border=3)
yearLabel.grid(row=1, column=3, padx=17)
yearEntry.grid(row=2, column=3, padx=17)

# the button
calcBtn = Button(root, text="What's my age?", font=("Poppins",12), padx=15, pady=2, bg="#ffc95c", command=calcFn)
calcBtn.grid(row=3, column=0, columnspan=4, pady=22)

# initializing the tkinter variable for the option menu
clicked = StringVar()
clicked.set("In Years")
# the option menu
timeMenu = OptionMenu(root, clicked, "In Years", "In Months", "In Days", "In Hours", "In Seconds")
timeMenu.grid(row=4, column=0, columnspan=4)

# the message label
msgLabel = Label(root, text="Don't judge me by my looks...just tell me your DOB, you'll see what I got!", font=("poppins",11), bg="#ff793b", fg="#dbfffe")
msgLabel.grid(row=5, column=0, columnspan=4, pady=17)

# the mainloop on exit terminates app
root.mainloop()