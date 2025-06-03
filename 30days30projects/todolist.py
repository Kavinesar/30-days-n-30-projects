from tkinter import *

tasks = []

def add():
    text = box.get()
    if text:
        tasks.append(text)
        box.delete(0, END)
        show()

def remove(i):
    tasks.pop(i)
    show()

def show():
    for w in area.winfo_children():
        w.destroy()
    for i, t in enumerate(tasks):
        row = Frame(area, bg="white")
        row.pack(fill="x", padx=5, pady=2)

        label = Label(row, text=t, anchor="w", bg="white")
        label.pack(side="left", fill="x", expand=True, padx=5)

        btn = Button(row, text="❌", bg="white", bd=0, command=lambda i=i: remove(i))
        btn.pack(side="right", padx=5)

win = Tk()
win.title("to-do")
win.geometry("300x400")
win.configure(bg="white")

box = Entry(win, width=25, bd=2, relief=FLAT)
box.pack(pady=10, padx=10)

add_btn = Button(win, text="add", command=add, bg="#4CAF50", fg="white", relief=FLAT, padx=10)
add_btn.pack(pady=5)

canvas = Canvas(win, bg="white", bd=0, highlightthickness=0)
scroll = Scrollbar(win, orient=VERTICAL, command=canvas.yview)
area = Frame(canvas, bg="white")

area.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=area, anchor="nw")
canvas.configure(yscrollcommand=scroll.set)

canvas.pack(side="left", fill="both", expand=True, padx=5)
scroll.pack(side="right", fill="y")

win.mainloop()
