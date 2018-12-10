import tkinter as tk

root = tk.Tk()
root.title("Calculator Subject Page")

from tkinter import *


SubjectPageLabel = tk.Label(root, text = "What general topic are you studying?")
Subjects = Listbox(root)
Subjects.insert(1, "Two Points on Line")
Subjects.insert(2, "Two Line Equations")
Subjects.insert(3, "Circle Equations")
Subjects.insert(4, "Triangle Equations")
Subjects.pack()

def submit():

	print("Submit pressed, Switching Pages...")


btn = tk.Button(root, text="submit", command=submit)
btn.pack()


root.mainloop()