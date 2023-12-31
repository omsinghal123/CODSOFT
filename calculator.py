from tkinter import *

def click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, str(current) + str(number))

def clear():
    entry.delete(0, END)

def equal():
    result = eval(entry.get())
    entry.delete(0, END)
    entry.insert(END, result)

root = Tk()
root.title("Calculator")

entry = Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_1 = Button(root, text="1", padx=20, pady=10, command=lambda: click(1), bg="light green")
button_2 = Button(root, text="2", padx=20, pady=10, command=lambda: click(2), bg="light green")
button_3 = Button(root, text="3", padx=20, pady=10, command=lambda: click(3), bg="light green")
button_4 = Button(root, text="4", padx=20, pady=10, command=lambda: click(4), bg="light green")
button_5 = Button(root, text="5", padx=20, pady=10, command=lambda: click(5), bg="light green")
button_6 = Button(root, text="6", padx=20, pady=10, command=lambda: click(6), bg="light green")
button_7 = Button(root, text="7", padx=20, pady=10, command=lambda: click(7),bg="light green")
button_8 = Button(root, text="8", padx=20, pady=10, command=lambda: click(8),bg="light green")
button_9 = Button(root, text="9", padx=20, pady=10, command=lambda: click(9),bg="light green")
button_0 = Button(root, text="0", padx=20, pady=10, command=lambda: click(0),bg="light green")

button_add = Button(root, text="+", padx=20, pady=10, command=lambda: click("+"))
button_subtract = Button(root, text="-", padx=20, pady=10, command=lambda: click("-"))
button_multiply = Button(root, text="*", padx=20, pady=10, command=lambda: click("*"))
button_divide = Button(root, text="/", padx=20, pady=10, command=lambda: click("/"))

button_equal = Button(root, text="=", padx=20, pady=10, command=equal)
button_clear = Button(root, text="C", padx=20, pady=10, command=clear)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=4, column=3)

root.mainloop()