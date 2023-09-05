import tkinter as tk
import random
import string

def password():
    password_length = int(length_entry.get())
    include_special_chars = special_chars_var.get()

    chars = string.ascii_letters + string.digits
    if include_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(password_length))
    password_label.config(text="Generated Password: " + password)

root = tk.Tk()
root.title("Password Generator")
root.geometry('650x500')

# Create and pack the widgets
length_label = tk.Label(root, text="Password Length:", font='ariel, 25 bold', width=18, bd=2, bg='light blue')
length_label.place(x=150, y=5)

length_entry = tk.Entry(root, font='ariel, 15', width=10)
length_entry.place(x=225, y=52)

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var)
special_chars_checkbox.place(x=150, y=100)

generate_button = tk.Button(root, text="Generate Password", command=password)
generate_button.place(x=150, y=140)

password_label = tk.Label(root, text="")
password_label.place(x=150, y=180)

root.mainloop()