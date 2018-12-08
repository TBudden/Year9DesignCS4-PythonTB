import tkinter as tk
import math

root = tk.Tk()
root.title("Calculator Variables Page")

from tkinter import *


var1 = IntVar()
Checkbutton(root, text="X", variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(root, text="Y", variable=var2).grid(row=1, sticky=W)

CheckListLabel = tk.Label(root, text = "Which Variables do you have?")
CheckListLabel.pack()

def submit():

	print("Submit")

btnSubmit = tk.Button(root, text="submit", command=submit)
btnSubmit.pack()

root.mainloop()