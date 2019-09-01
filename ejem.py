import tkinter as tk
from tkinter import ttk


def step():
    BarVolVal_1.step(dir)
    mGui.after(10, step)

def change_dir():
    global dir
    dir *= -1
    mGui.after(2000, change_dir)

mGui = tk.Tk()
dir = 1
BarVolVal_1 = ttk.Progressbar(mGui, orient='vertical', length=100, mode='determinate')
BarVolVal_1.pack()
step()
mGui.after(3000, change_dir)
mGui.mainloop()