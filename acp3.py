import tkinter as tk

def convert_to_cm():
    try:
        inches = float(entry.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{centimeters:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Set up the main window
root = tk.Tk()
root.title("Height Converter: Inches to Centimeters")
root.geometry("300x150")

# Input label and entry
tk.Label(root, text="Enter height in inches:").pack(pady=5)
entry = tk.Entry(root)
entry.pack()

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_to_cm)
convert_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()