import math
from tkinter import *

root = Tk()
root.title("Calculator")

panel = Entry(root, borderwidth=3, width=62)
panel.grid(row=0, column=0, columnspan=4)

button_1 = Button(root, text="1", padx=40, pady=30, command=lambda: button_1(1))
button_2 = Button(root, text="2", padx=40, pady=30, command=lambda: button_2(2))
button_3 = Button(root, text="3", padx=40, pady=30, command=lambda: button_3(3))
button_4 = Button(root, text="4", padx=40, pady=30, command=lambda: button_4(4))
button_5 = Button(root, text="5", padx=40, pady=30, command=lambda: button_5(5))
button_6 = Button(root, text="6", padx=40, pady=30, command=lambda: button_6(6))
button_7 = Button(root, text="7", padx=40, pady=30, command=lambda: button_7(7))
button_8 = Button(root, text="8", padx=40, pady=30, command=lambda: button_8(8))
button_9 = Button(root, text="9", padx=40, pady=30, command=lambda: button_9(9))
button_0 = Button(root, text="0", padx=40, pady=30, command=lambda: button_0(0))

def add_button():
    global num1
    global math
    math = "addition"
    num1 = int(panel.get())
    panel.delete(0, END)

def substract_button():
    global num1
    global math
    math = "subtraction"
    num1 = int(panel.get())
    panel.delete(0, END)

def multiply_button():
    global num1
    global math
    math = "multiplication"
    num1 = int(panel.get())
    panel.delete(0, END)

def divide_button():
    global num1
    global math
    math = "division"
    num1 = int(panel.get())
    panel.delete(0, END)

def equal_button():
    num2 = int(panel.get())
    panel.delete(0, END)

    if math == "addition":
        result = int(num1) + int(num2)
        panel.insert(0, result)

    elif math == "subtraction":
        result = int(num1) - int(num2)
        panel.insert(0, result)

    elif math == "multiplication":
        result = int(num1) * int(num2)
        panel.insert(0, result)

    elif math == "division":
        result = int(num1) / int(num2)
        panel.insert(0, result)

def clear_button():
    panel.delete(0, END)

clear_button = Button(root, text="clear", pady=30, padx=80, command=clear_button)
add_button = Button(root, text="+", padx=40, pady=30, command=add_button)
substract_button = Button(root, text="-", padx=40, pady=30, command=substract_button)
multiply_button = Button(root, text="x", padx=40, pady=30, command=multiply_button)
divide_button = Button(root, text="%", padx=40, pady=30, command=divide_button)
equal_button = Button(root, text="=", padx=40, pady=30, command=equal_button)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=2)
equal_button.grid(row=5, column=2)

clear_button.grid(row=4, column=0, columnspan=2)
add_button.grid(row=1, column=3)
substract_button.grid(row=2, column=3)
multiply_button.grid(row=3, column=3)
divide_button.grid(row=4, column=3)

# button functions
def button_1(number):
    current = panel.get()
    num = str(current) + str(number)
    panel.delete(0, END)
    panel.insert(0, num)

def button_2(number):
    current = panel.get()
    num = str(current) + str(number)
    panel.delete(0, END)
    panel.insert(0, num)

def button_3(number):
    current = panel.get()
    num = str(current) + str(number)
    panel.delete(0, END)
    panel.insert(0, num)

def button_4(number):
    current = panel.get()
    num = str(current) + str(number)
    panel.delete(0, END)
    panel.insert(0, num)

def button_5(number):
    current = panel.get()
    num = str(current) + str(number)
    panel.delete(0, END)
    panel.insert(0, num)

def button_6(number):
    current = panel.get()
    num = str(current) + str(number)
    panel.delete(0, END)
    panel.insert(0, num)

def button_7(number):
    current = panel.get()
    num = str(current) + str(number)
    panel.delete(0, END)
    panel.insert(0, num)

def button_8(number):
    current = panel.get()
    num = str(current) + str(number)
    panel.delete(0, END)
    panel.insert(0, num)

def button_9(number):
    current = panel.get()
    num = str(current) + str(number)
    panel.delete(0, END)
    panel.insert(0, num)

def button_0(number):
    current = panel.get()
    num = str(current) + str(number)
    panel.delete(0, END)
    panel.insert(0, num)

root.mainloop()
