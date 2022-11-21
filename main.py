from tkinter import *
from random import *


myInterface = Tk()
screen = Canvas(myInterface, width=400, height=400, background="grey")
screen.pack()

size = 100
x, y = 0, 0
colors = ["white", "black"]

for i in range(8):
	for j in range(8):
		screen.create_rectangle(x, y, x+size, y+size, fill=colors[j%2], width=0)
		x += size
	x = 0	
	y += size
	colors = colors[::-1]
