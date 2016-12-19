#! /usr/bin/env python
import matplotlib
matplotlib.use('TkAgg')

from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np
import pylab as pl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import sys

class App(Frame):

	def __init__(self, master):
		
		"""Initialise the base class"""
		Frame.__init__(self,master)
		"""Set the Window Title"""
		self.master.title("RXF Data Fit")
		self.configure(height=200,width=200)
		"""Display the main window with a little bit of padding"""
		self.grid(padx=15, pady=15,sticky=N+S+E+W)       
		#Create the Menu base
		self.menu = Menu(self)
		#Add the Menu
		self.master.config(menu=self.menu)
		self.menu.add_command(label="Open", command=self.fileOpen)
		self.menu.add_command(label="Help", command=self.Simple)
		self.menu.add_command(label="Quit", command=self.exitProgram)
		self.pack()
		f = Figure(figsize=(5,4), dpi=100)
		canvas=FigureCanvasTkAgg(f,master=root)
		canvas.show()
		canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
		toolbar = NavigationToolbar2TkAgg( canvas, root )
		toolbar.update()
		canvas._tkcanvas.pack(side="top", fill="both", expand=1)		


		xRangeLabel=Label(root,text="X Range")
		xRangeLabel.pack()		
	
		replotButton=Button(root, text="Replot", command=self.replot)
		replotButton.pack()
	
		clearButton=Button(root,text="Clear Plot", command=self.clearPlot)
		clearButton.pack(padx=20,pady=5)

	
	def fileOpen(self):
		filename=askopenfilename(filetypes=[("Data Files","*.dat *.DAT")])
		data=np.loadtxt(filename)
		j=0
		x=[]
		for i in data:
			xnew=[j]
			x=x+xnew
			j=j+1
		pl.plot(x,data, 'ro')
		pl.title(filename)
		pl.xlabel("ADC Counts")
		pl.ylabel("Occurences")
		pl.show()
	#end of fileOpen

	def Menu(self):
		tkMessageBox.showinfo("Menu", "Menu")   
	def Simple(self):
		tkMessageBox.showinfo("Simple","Simple")  
	def exitProgram(self):
		root.destroy()

	def replot(self, event):
		print "Not really."
	def clearPlot(self,event):
		print "not cleared."   	

if __name__ == "__main__":
	root = Tk()
	app = App(root)
	root.mainloop()
