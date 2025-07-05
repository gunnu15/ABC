import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

button = tk.Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

root.mainloop()