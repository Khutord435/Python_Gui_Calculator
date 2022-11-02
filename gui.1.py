from tkinter import *

#first_num = None
#operation = None
#second_num = None

def button_one():
    entry1.insert(END, "1")
def button_two():
    entry1.insert(END, "2")
def button_three():
    entry1.insert(END, "3")
def button_four():
    entry1.insert(END, "4")
def button_five():
    entry1.insert(END, "5")
def button_six():
    entry1.insert(END, "6")
def button_seven():
    entry1.insert(END, "7")
def button_eight():
    entry1.insert(END, "8")
def button_nine():
    entry1.insert(END, "9")
def button_zero():
    entry1.insert(END, "0")
def buttonneg():
    entry1.insert(0, "-")
def button_decimal():
    entry1.insert(END, ".")

def button_plus():
    first_num = entry1.get()
    print(first_num)
    operation = "+"
    print(operation)
    entry1.delete(0, END)
def button_minus():
    first_num = entry1.get()
    print(first_num)
    operation = "-"
    print(operation)
    entry1.delete(0, END)
def button_times():
    first_num = entry1.get()
    print(first_num)
    operation = "*"
    print(operation)
    entry1.delete(0, END)
def button_divide():
    first_num = entry1.get()
    print(first_num)
    operation = "/"
    print(operation)
    entry1.delete(0, END)
def button_ans():
    second_num = entry1.get()
    print(second_num)
    print(first_num)
    print(operation)
    
root = Tk()
entry1 = Entry(root, width=35)
entry1.grid(row=0,column=0, columnspan=4)

button1 = Button(root, text="1", padx=18, pady=5, command= button_one).grid(row=3,column=0)
button2 = Button(root, text="2", padx=18, pady=5, command= button_two).grid(row=3,column=1)
button3 = Button(root, text="3", padx=18, pady=5, command= button_three).grid(row=3,column=2)
button4 = Button(root, text="4", padx=18, pady=5, command= button_four).grid(row=2,column=0)
button5 = Button(root, text="5", padx=18, pady=5, command= button_five).grid(row=2,column=1)
button6 = Button(root, text="6", padx=18, pady=5, command= button_six).grid(row=2,column=2)
button7 = Button(root, text="7", padx=18, pady=5, command= button_seven).grid(row=1,column=0)
button8 = Button(root, text="8", padx=18, pady=5, command= button_eight).grid(row=1,column=1)
button9 = Button(root, text="9", padx=18, pady=5, command= button_nine).grid(row=1,column=2)
button0 = Button(root, text="0", padx=18, pady=5, command= button_zero).grid(row=4,column=1)

buttonnegpos = Button(root, text="-", padx=19, pady=5, command= buttonneg).grid(row=4, column=0)
butonperiod = Button(root, text=".", padx=19.4, pady=5, command= button_decimal).grid(row=4,column=2)
buttonplus = Button(root, text="+", padx=18, pady=5, command= button_plus).grid(row=1,column=3)
buttonminus = Button(root, text="-", padx=18, pady=5, command= button_minus).grid(row=2,column=3)
buttontimes = Button(root, text="x", padx=18, pady=5, command= button_times).grid(row=3,column=3)
buttondivide = Button(root, text="÷", padx=18, pady=5, command= button_divide).grid(row=4,column=3)
buttonans =  Button(root, text="=", padx=100, pady=5, command= button_ans).grid(row=5,column=0, columnspan=4)

root.mainloop()
