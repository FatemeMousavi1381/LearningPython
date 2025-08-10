import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password(length) : 

    digits = random.choice(string.digits)
    upper_case = random.choice(string.ascii_uppercase)
    lower_case = random.choice(string.ascii_lowercase)
    special_char = random.choice('\!@#$%^&*()_+=-?|:;,./')
    other_char = random.choices(string.ascii_letters + string.digits + '\!@#$%^&*()_+=-?|:;,./' , k=length - 4) 

    password_list = [digits , upper_case , lower_case , special_char ] + other_char
    random.shuffle(password_list)

    password = ''.join(password_list)
    return password 

def generate():
        try : 
            length =int(entry.get())

            if length >= 20 :
                messagebox.showerror("Error!!!","Password length must be less than 20.")
                return ""   
        except ValueError :
            messagebox.showerror("Error!!!","Invalid input !!! Please enter numbers only.")
            return 
        pwd = generate_password(length)
        if pwd : 
            result_var.set(pwd)
        

root = tk.Tk()
root.title('Password Generator')
root.geometry('400x150')


tk.Label(root, text="Enter password length:" , font="bold" , fg="Green" ).pack(pady=5)
entry = tk.Entry(root)
entry.pack()


btn = tk.Button(root, text="Generate Password" , fg="Green" , command=generate)
btn.pack(pady=5)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Aria", 12 , "bold"), fg="crimson")
result_label.pack(pady=5)

root.mainloop()
            
