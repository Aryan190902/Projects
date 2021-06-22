from tkinter import *

root= Tk()

root.title("Simple Calculator")


en = Entry(root, width = 40, borderwidth= 10)
en.grid(row=0, column=0, columnspan=3, padx = 10, pady = 10)
def Butt(number):
    currentNumber = en.get()
    en.delete(0, END)
    en.insert(0, str(currentNumber) + str(number))

def Add():
    num = en.get()
    en.delete(0, END)
    global cnt
    global phrase 
    cnt = float(num)
    phrase = "+"

def Clear():
    en.delete(0,END)

def Equal():
    sec_number = en.get()
    en.delete(0, END)
    if phrase == "+":
        en.insert(0, float(cnt) + float(sec_number))
    elif phrase == "-":
        en.insert(0, float(cnt) - float(sec_number))
    elif phrase == "x":
        en.insert(0, float(cnt) * float(sec_number))
    elif phrase == "/":
        en.insert(0, float(int(cnt)/float(sec_number)))

def Subs():
    num = en.get()
    en.delete(0, END)
    global cnt
    global phrase 
    cnt = float(num)
    phrase = "-"

def Divide():
    num = en.get()
    en.delete(0, END)
    global cnt
    global phrase 
    cnt = float(num)
    phrase = "/"

def Multiply():
    num = en.get()
    en.delete(0, END)
    global cnt
    global phrase 
    cnt = float(num)
    phrase = "x"

Butt1 = Button(root, text = "1", padx = 40, pady = 40, command=lambda: Butt(1))
Butt2 = Button(root, text = "2", padx = 40, pady = 40, command=lambda: Butt(2))
Butt3 = Button(root, text = "3", padx = 40, pady = 40, command=lambda: Butt(3))
Butt4 = Button(root, text = "4", padx = 40, pady = 40, command=lambda: Butt(4))
Butt5 = Button(root, text = "5", padx = 40, pady = 40, command=lambda: Butt(5))
Butt6 = Button(root, text = "6", padx = 40, pady = 40, command=lambda: Butt(6))
Butt7 = Button(root, text = "7", padx = 40, pady = 40, command=lambda: Butt(7))
Butt8 = Button(root, text = "8", padx = 40, pady = 40, command=lambda: Butt(8))
Butt9 = Button(root, text = "9", padx = 40, pady = 40, command=lambda: Butt(9))
Butt0 = Button(root, text = "0", padx = 40, pady = 40, command=lambda: Butt(0))

add_butt = Button(root, text="+", padx = 40, pady = 40, command=Add)
clear_butt= Button(root, text="AC",padx = 40, pady = 40,  command=Clear)
equal_butt = Button(root, text="=", padx = 80, pady = 40, command=Equal)
subs_butt = Button(root, text="-", padx = 40, pady= 40, command=Subs)
div_butt = Button(root, text="/", padx = 40, pady = 40, command=Divide)
multi_butt = Button(root, text="x", padx = 80, pady = 40, command=Multiply)

Butt1.grid(row=3, column=0)
Butt2.grid(row=3, column=1)
Butt3.grid(row=3, column=2)
Butt4.grid(row=2, column=0)
Butt5.grid(row=2, column=1)
Butt6.grid(row=2, column=2)
Butt7.grid(row=1, column=0)
Butt8.grid(row=1, column=1)
Butt9.grid(row=1, column=2)
Butt0.grid(row=4, column=0)

add_butt.grid(row=4, column=1)
subs_butt.grid(row=4, column= 2)
clear_butt.grid(row=5, column= 2)
equal_butt.grid(row=5, column= 0, columnspan=2)
multi_butt.grid(row=6, column= 0, columnspan=2)
div_butt.grid(row= 6, column=2)


root.mainloop()
