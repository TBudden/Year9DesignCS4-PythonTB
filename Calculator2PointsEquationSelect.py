import tkinter as tk
import math
root = tk.Tk()

from tkinter import *

def submit():

	print("Submit")

root = tk.Tk()
root.title("Calculator Home Page")

EquationsLabel = tk.Label(root, text = "Equations:")
EquationsLabel.pack()

Equations = Listbox(root)
Equations.insert(1, "Midpoint([{x1+x2}/2,{y1+y2}/2])")
Equations.insert(2, "Slope(y2-y1/x2-x1)",)
Equations.insert(3, "Line Length(√[x2-x1]²+[y2-y1]²)")
Equations.pack()


btn = tk.Button(root, text="submit", command=submit)
btn.pack()

root.mainloop() 