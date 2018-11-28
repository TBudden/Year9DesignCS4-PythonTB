import tkinter as tk
import math

def change(*args):
	print("running change")
	print(var.get())

def submit():

	print("Submit")

root = tk.Tk()
root.title("Calculator Home Page")

Equations = [
"Slope Y-Int Form(Y=mx+b)",
 "Slope(y2-y1/x2-x1)"
 ]

var = tk.StringVar(root)
var.set(Equations[0])
var.trace("w",change)

dropDownMenu = tk.OptionMenu(root,var, Equations[0],Equations[1])
dropDownMenu.pack()

btn = tk.Button(root, text="submit", command=submit)
btn.pack()

root.mainloop()