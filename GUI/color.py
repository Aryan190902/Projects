from tkinter import *
from random import choice, random
import random
import time


root = Tk()
root.title("Color Game")
root.geometry("600x600")
customFont = ('Comic Sans MS', 20)
custonFont1 = ('Comic Sans MS', 30)
x = IntVar(root, value=0)

game_over = False

lst = ['red', 'blue', 'green', 'yellow', 'pink', 'orange', 'grey', 'black',
 'gold', 'cyan', 'purple']
textLst = sorted(lst)
textColor = choice(lst)
textSelect = choice(textLst)
scLabel = Label(root, text="Score", font= customFont)
scLabel.pack()
score = Label(root, text="Score:", font=customFont
, padx= 30, pady=30, textvariable=x)
score.pack(side='top')
show = Label(root, text = textSelect, font=custonFont1, fg = textColor,
                padx = 50, pady = 25)

show.configure(anchor=CENTER)
show.pack()
randomSeed = [69, 420, 777, 123, 50, 100, 10000]
en = Entry(root, font=customFont, textvariable=StringVar)
time_limit = 15
time_left = 15

def correctColor(answer):
    en.delete(0, END)
    global x
    if answer == show['fg']:
        global time_left
        x.set(x.get()+50)
        if time_left<=13:
            time_left += 2
        else:
            time_left =15
    else:
        global game_over
        game_over = True
        en.destroy()
        score.destroy()
        Submit.destroy()
        show.destroy()
        scLabel['text'] = "Final Score:"
        lose = Label(root, text= str(x), textvariable=x, font= custonFont1)
        lose.pack()
        
en.pack()

def submit():
    correctColor(en.get())
    show['text'] = choice(textLst)
    show['fg'] = choice(lst)

Submit = Button(root, text="Submit", command=submit)
Submit.pack()
#timer
start_time = time.time()

time_label = Label(root, text="Time Left:", font=customFont)

def Timer():
    global time_left
    if time_left>0:
        if game_over == False:
            time_left -= 1
            time_shower.config(text= str(time_left))
            time_shower.after(1000, Timer)
        else:
            en.destroy()
            score.destroy()
            Submit.destroy()
            show.destroy()
            time_shower.destroy()
            time_label.destroy()
    else:
        en.destroy()
        score.destroy()
        Submit.destroy()
        show.destroy()
        time_shower.destroy()
        time_label.destroy()
        scLabel['text'] = "Final Score:"
        scLabel['pady'] = 50
        lose = Label(root, text=str(x), textvariable=x, font= custonFont1, pady = 50)
        lose.pack()

time_shower = Label(root, text='', font = customFont)
Timer()
time_label.pack()
time_shower.pack()

root.mainloop()