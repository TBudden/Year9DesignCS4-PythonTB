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
"select",
"Slope Y-Int Form(Y=mx+b)",
 "Slope(y2-y1/x2-x1)",
 "Line Length(√[x2-x1]²+[y2-y1]²)",
 ]

var = tk.StringVar(root)
var.set(Equations[0])
var.trace("w",change)


dropDownMenuLabel = tk.Label(root, text = "Equations:")
dropDownMenuLabel.pack()

dropDownMenu = tk.OptionMenu(root,var, Equations[0],Equations[1],Equations[2],Equations[3], width=20, height=10, borderwidth=3)
dropDownMenu.pack()

btn = tk.Button(root, text="submit", command=submit)
btn.pack()

root.mainloop()