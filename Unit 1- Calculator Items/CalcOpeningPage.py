import tkinter as tk
root = tk.Tk()

root.title("Calculator Opening Page")

FirstPageText = tk.Label(root, text = "This program is intended to solve basic questions from Chapters 1-2 of the Principles of Mathematics 10 textbook and, more generally, solve questions in Linear Systems and Analytic Geometry. Do you wish to continue?")
FirstPageText.pack()

def Yes():

	print("Yes")

def No():

	NoText = tk.Label(root, text = "Okay, goodbye!")
	NoText.pack()

btnYes = tk.Button(root, text="Yes", command=Yes)
btnYes.pack()

btnNo = tk.Button(root, text="No", command=No)
btnNo.pack()

root.mainloop()