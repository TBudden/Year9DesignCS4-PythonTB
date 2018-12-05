import tkinter as tk
import math

btn = tk.Button(root, text="submit", command=submit)
btn.pack()

output = tk.Text(root, width=20, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()

root.mainloop()