from tkinter import *
import random, string
from tkinter import messagebox
import pyperclip
import re


# UI + Component
window = Tk() 
window.resizable(0,0)
window.title("Make My Password")
canvas=Canvas(window, width=400, height=400)
canvas.configure(background="light grey")
canvas.pack()

# Image logo 
logo_img=PhotoImage(file="passwordGenerator.png")
logo_img=logo_img.subsample(x=4, y=4) # Resize image
canvas.create_image(200, 70, image=logo_img)

# Title
l_title=Label(master=canvas,
            text="Random Password Generator",
            font="Elephant 13 bold",
            bg="light grey")

canvas.create_line(50, 170, 351, 170, fill='grey', width=2)

l_title2=Label(master=canvas,
            text="Check My Password",
            font="Elephant 13 bold",
            bg="light grey")

canvas.create_line(91, 310, 308, 310, fill='grey', width=2)

# Label
# Password Length
pass_label=Label(master=canvas,
                text="Password Length:",
                font="Elephant 10 bold",
                bg="light grey")

pass_len = IntVar()
length=Spinbox(master=canvas,
            from_=8,
            to_=32,
            textvariable=pass_len,
            width=13)

# Input your password 
pass_input=Label(master=canvas,
                text="Input Your Password:",
                font="Elephant 10 bold",
                bg="light grey")

canvas.create_window(200, 147, window=l_title)
canvas.create_window(200, 290, window=l_title2)
canvas.create_window(100, 190, window=pass_label)
canvas.create_window(113, 330, window=pass_input)
canvas.create_window(310, 189, window=length)

# Generate Function
pass_str=StringVar()
def generate_password():
    pass_=''
    for x in range(0, 4):
        pass_=random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()-4):
        pass_=pass_+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(pass_)

# Copy Password Function
buttonClicked=False
def copy_pass():
    if not buttonClicked:
        pyperclip.copy(pass_str.get()) 
        return messagebox.showinfo(title="", message="Password copied")

# Checker Function
pass_checker=StringVar()
def passwordChecker():
    message=''
    if(len(str(pass_checker.get())) >= 8):
        if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,32})',str(pass_checker.get())))==True):
            message=messagebox.showinfo(title="Password Status", message="Your Password is Strong!")
        elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,32})',str(pass_checker.get())))==True):
            message=messagebox.showinfo(title="Password Status", message="Your Password is Weak!")
    return message

# Button
# Generate btn.
btn_generate=Button(master=canvas,
                    text="Generate",
                    command=generate_password)

# Copy btn.
btn_copy=Button(master=canvas,
                text="Copy",
                command=copy_pass)

btn_checkMyPass=Button(master=canvas,
                    text="Check Password",
                    command=passwordChecker)

canvas.create_window(250, 260, window=btn_generate)
canvas.create_window(140, 260, window=btn_copy)
canvas.create_window(205, 364, window=btn_checkMyPass)

# Entry 
get_length_pass=Entry(master=canvas,
                    textvariable=pass_str,
                    width=35)

get_check_pass=Entry(master=canvas,
                    textvariable=pass_checker,
                    width=20)

canvas.create_window(200, 225, window=get_length_pass)
canvas.create_window(288, 329, window=get_check_pass)


canvas.mainloop()