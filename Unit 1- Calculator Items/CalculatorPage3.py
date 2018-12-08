import tkinter as tk
import math

root = tk.Tk()
root.title("Calculator Output Page")

def submit():

	print("Submit")

btn = tk.Button(root, text="submit", command=submit)
btn.pack()

outputBox = tk.Text(root, width=20, height=10, borderwidth=3, relief=tk.GROOVE)
outputBox.config(state="disabled")
outputBox.pack()

root.mainloop()