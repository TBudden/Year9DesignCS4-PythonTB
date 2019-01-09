import tkinter as tk
import math


def submit():

	print("Calculating...")

	x1 = float(entr.get())
	x2 = float(enth.get())
	y1 = float(ente.get())
	y2 = float(entt.get())

	mx = round((x1 + x2)/2,2)
	midpointx.append(mx)
	my = round((y1 + y2)/2,2)
	midpointy.append(my)


	m = round((y2 - y1)/(x2 - x1),2)
	

	l = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	print("Midpoint:" + "("+str(mx)+","+str(my)+")")
	print ("Slope:" + (m))
	print ("Length:" + (l))

	#String construct 
	out = "Results\n"
	out = out + "M("+str(mx)+","+str(my)+")"
	out2 = "Midpoint" + str(m)
	out3 = "Length" + str(l)


	output.config(state = "normal")
	output.delete("1.0",tk.END)
	output.insert(tk.END,out, out2, out3)
	output.config(state = "disabled")

	print("Midpoint X:" + (midpointx))
	print("Midpoint Y:" + (midpointy)
midpointx = []
midpointy = []


root = tk.Tk()

root.title("Final Calculation")

Point1XLabel = tk.Label(root, text = "Point 1 X:")
Point1XLabel.pack()

entr = tk.Entry(root)
entr.pack()


Point1YLabel = tk.Label(root, text = "Point 1 Y:")
Point1YLabel.pack()

ente = tk.Entry(root)
ente.pack()

Point2XLabel = tk.Label(root, text = "Point 2 X:")
Point2XLabel.pack()

enth = tk.Entry(root)
enth.pack()

Point2YLabel = tk.Label(root, text = "Point 2 Y:")
Point2YLabel.pack()

entt = tk.Entry(root)
entt.pack()


btn = tk.Button(root, text="calculate", command=submit)
btn.pack()

output = tk.Text(root, height = 6, width=20, borderwidth=1, relief=tk.GROOVE)
output.config(state ="disabled")
output.pack()



root.mainloop()