import tkinter as tk
import math

root = tk.Tk()
root.title("Calculator Variables Page")

labr = tk.Label(root, text="Variable 1")
labr.pack

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="Variable 2")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="submit", command=submit)
btn.pack()

root.mainloop()