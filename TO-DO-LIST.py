from tkinter import *
from tkinter import messagebox
#------------------ADD TASK-------------------
def add_task():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)

#------------------DELETE TASK-----------------
def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass

def save_tasks():
    tasks = listbox.get(0, END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def edit_task():
    try:
        index = listbox.curselection()
        task = listbox.get(index)
        entry.delete(0, END)
        entry.insert(END, task)
        listbox.delete(index)
    except:
        pass

root = Tk()
root.title("To-Do List")

frame = Frame(root)
frame.pack(pady=10)

listbox = Listbox(frame, width=50)
listbox.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = Entry(root, font=("Arial", 12))
entry.pack(pady=10)

add_button = Button(root, text="Add Task", command=add_task, bg="light blue")
add_button.pack(pady=5)

delete_button = Button(root, text="Delete Task", command=delete_task,bg="light blue")
delete_button.pack(pady=5)

save_button = Button(root, text="Save Tasks", command=save_tasks, bg="light blue")
save_button.pack(pady=5)

edit_button = Button(root, text="Edit Task", command=edit_task, bg="light blue")
edit_button.pack(pady=5)

root.mainloop()