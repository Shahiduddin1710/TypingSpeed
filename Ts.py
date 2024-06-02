from words import words
from tkinter import *
import random
from tkinter import messagebox

def slider():
    global count, sliderwords
    text = "Welcome to Typing Speed Increaser"
    if count >= len(text):
        count = 0
        sliderwords = ""
    sliderwords += text[count]
    count += 1
    fontlabel.configure(text=sliderwords)
    fontlabel.after(150, slider)

def time():
    global timer, score, miss
    if timer > 11:
        pass
    else:
        timerlabelcount.configure(fg="red")
    if timer > 0:
        timer -= 1
        timerlabelcount.configure(text=timer)
        timerlabelcount.after(1000, time)
    else:
        gameinstruction.configure(
            text="Hit = {} | Miss = {} | Total Score = {}".format(
                score, miss, score - miss
            )
        )
        rr = messagebox.askretrycancel("Notification", "Wanna Play Again!!!!")
        if rr == True:
            score = 0
            miss = 0
            timer = 60
            timerlabelcount.configure(text=timer)
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)
            wordentry.delete(0, END)

def startgame(event):
    global score, miss
    if timer == 60:
        time()
    gameinstruction.configure(text="")
    startlabel.configure(text="")
    if wordentry.get() == wordlabel["text"]:
        score += 1
        scorelabelcount.configure(text=score)
    else:
        miss += 1
    random.shuffle(words)
    wordlabel.configure(text=words[0])
    wordentry.delete(0, END)

###############################################
root = Tk()
root.geometry("800x600+400+100")
root.configure(bg="#1e1e1e")
root.title("Typing Speed Increaser")
root.iconbitmap("typing speed image.ico")

##############################################

score = 0
miss = 0
timer = 60
count = 0
sliderwords = ""

#################################################################
fontlabel = Label(
    root, text="", font=("Helvetica", 25, "bold"), bg="#1e1e1e", fg="#ff79c6", width=40
)
fontlabel.place(x=10, y=10)
slider()

startlabel = Label(
    root,
    text="Let's begin!!!",
    font=("Helvetica", 30, "bold"),
    bg="#1e1e1e",
    fg="#8be9fd",
)
startlabel.place(x=275, y=50)

random.shuffle(words)
wordlabel = Label(
    root, text=words[0], font=("Helvetica", 45, "bold"), bg="#1e1e1e", fg="#50fa7b"
)
wordlabel.place(x=350, y=240)

scorelabel = Label(
    root, text="Your Score:", font=("Helvetica", 25, "bold"), bg="#1e1e1e", fg="#ff5555"
)
scorelabel.place(x=10, y=100)

scorelabelcount = Label(
    root, text=score, font=("Helvetica", 25, "bold"), bg="#1e1e1e", fg="#bd93f9"
)
scorelabelcount.place(x=200, y=180)

timerlabel = Label(
    root, text="Time Left:", font=("Helvetica", 25, "bold"), bg="#1e1e1e", fg="#ff5555"
)
timerlabel.place(x=600, y=100)

timerlabelcount = Label(
    root, text=timer, font=("Helvetica", 25, "bold"), bg="#1e1e1e", fg="#bd93f9"
)
timerlabelcount.place(x=600, y=180)

gameinstruction = Label(
    root,
    text="Type the Word and hit enter button",
    font=("Helvetica", 25, "bold"),
    bg="#1e1e1e",
    fg="#f1fa8c",
)
gameinstruction.place(x=150, y=500)

########################################################################

wordentry = Entry(root, font=("Helvetica", 25, "bold"), bd=10, justify="center")
wordentry.place(x=250, y=330)
wordentry.focus_set()

# Add the new label for the message
creditlabel = Label(
    root,
    text="Made By Mohammed Shahiduddin Shaikh",
    font=("Helvetica", 15, "bold"),
    bg="#1e1e1e",
    fg="#f8f8f2"
)
creditlabel.place(x=250, y=560)

#################################################################
root.bind("<Return>", startgame)
root.mainloop()
