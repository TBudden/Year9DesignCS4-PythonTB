import tkinter as tk
import math
root = tk.Tk()

from tkinter import *

top = Tk()

def submit():

	print("Submit")

root = tk.Tk()
root.title("Calculator Home Page")

Equations = Listbox(top)
Equations.insert(1, "Midpoint([{x1+x2}/2,{y1+y2}/2])")
Equations.insert(2, "Slope(y2-y1/x2-x1)",)
Equations.insert(3, "Line Length(√[x2-x1]²+[y2-y1]²)")
Equations.pack()


EquationsLabel = tk.Label(root, text = "Equations:")
EquationsLabel.pack()


btn = tk.Button(root, text="submit", command=submit)
btn.pack()

root.mainloop()