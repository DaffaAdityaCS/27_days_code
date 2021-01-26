from tkinter import *
# you need install tkinter first

# Showing window
root = Tk()
root.title("Super Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# def logic
def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_plus():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "devision":
        e.insert(0, f_num / int(second_number))

def button_subract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "devision"
    f_num = int(first_number)
    e.delete(0, END)


# Define Buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_add(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_add(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_add(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_add(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_add(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_add(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_add(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_add(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_add(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_add(0))

button_ad = Button(root, text="+", padx=39, pady=20, command= button_plus)
button_subractt = Button(root, text="-", padx=41, pady=20, command= button_subract)
button_multiplyy = Button(root, text="*", padx=40, pady=20, command= button_multiply)
button_dividee = Button(root, text="%", padx=41, pady=20, command= button_divide)
button_equall = Button(root, text="=", padx=91, pady=20, command= button_equal)
button_clearr = Button(root, text="Clear", padx=79, pady=20, command= button_clear)


# put the buttons
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=1)
button_multiplyy.grid(row=4, column=0)
button_dividee.grid(row=4, column=2)

button_clearr.grid(row=5, column=1, columnspan=2)
button_ad.grid(row=5, column=0)

button_equall.grid(row=6, column=1, columnspan=2)
button_subractt.grid(row=6, column=0)


# loop program
root.mainloop()