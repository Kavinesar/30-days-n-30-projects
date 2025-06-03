from tkinter import *
import random
import string

def gen(level):
    if level == "weak":
        chars = string.ascii_lowercase
        size = 6
    elif level == "medium":
        chars = string.ascii_letters + string.digits
        size = 8
    else:
        chars = string.ascii_letters + string.digits + string.punctuation
        size = 12
    pwd = ''.join(random.choice(chars) for _ in range(size))
    show(pwd)

def show(p):
    out.delete(0, END)
    out.insert(0, p)

win = Tk()
win.title("passwords")
win.geometry("300x250")
win.configure(bg="#f2f2f2")

label = Label(win, text="pick strength", bg="white", fg="#333", font=("Arial", 12))
label.pack(pady=10)

btn1 = Button(win, text="weak", width=12, bg="green", fg="white", activebackground="#ff4d4d", command=lambda: gen("weak"))
btn1.pack(pady=5)

btn2 = Button(win, text="medium", width=12, bg="yellow", fg="white", activebackground="#e69500", command=lambda: gen("medium"))
btn2.pack(pady=5)

btn3 = Button(win, text="strong", width=12, bg="red", fg="white", activebackground="#33aa33", command=lambda: gen("strong"))
btn3.pack(pady=5)

out = Entry(win, width=28, justify="center", bd=2, relief=FLAT, font=("Courier", 12))
out.pack(pady=20)

win.mainloop()
