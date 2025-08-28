# Simple Tkinter GUI example
import tkinter as tk

root = tk.Tk()
root.title("My GUI")

label = tk.Label(root, text="Hello, GUI!")
label.pack()

root.mainloop()