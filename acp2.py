import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        
        birth_date = date(year, month, day)
        today = date.today()

        if birth_date > today:
            messagebox.showerror("Error", "Birth date cannot be in the future.")
            return

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"You are {age} years old.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for date.")

# GUI setup
root = tk.Tk()
root.title("Age Calculator")

# Labels and entries for day, month, year
tk.Label(root, text="Day:").grid(row=0, column=0, padx=10, pady=5)
entry_day = tk.Entry(root)
entry_day.grid(row=0, column=1)

tk.Label(root, text="Month:").grid(row=1, column=0, padx=10, pady=5)
entry_month = tk.Entry(root)
entry_month.grid(row=1, column=1)

tk.Label(root, text="Year:").grid(row=2, column=0, padx=10, pady=5)
entry_year = tk.Entry(root)
entry_year.grid(row=2, column=1)

# Button to calculate age
calc_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calc_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to display result
result_label = tk.Label(root, text="Your age will appear here.")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Start the GUI
root.mainloop()