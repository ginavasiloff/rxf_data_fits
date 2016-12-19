#! /usr/bin/env python
import matplotlib
matplotlib.use('TkAgg')

from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np

class App(Frame):
	def __init__(self, master):
		"""Initialise the base class"""
		Frame.__init__(self,master)
		"""Set the Window Title"""
		self.master.title("RXF Data Fit")
		self.configure(height=1,width=200)
		"""Display the main window with a little bit of padding"""
		self.grid(padx=15, pady=15,sticky=N+S+E+W)
		#Create the Menu base
		self.menu = Menu(self)
		#Add the Menu
		self.master.config(menu=self.menu)
		self.menu.add_command(label="Open", command=self.fileOpen)
		helpmenu=Menu(self.menu,tearoff=0)
		helpmenu.add_command(label="About",command=self.about)
		helpmenu.add_command(label="Manual",command=self.manual)
		self.menu.add_cascade(label="Help", menu=helpmenu)
		self.menu.add_command(label="Quit", command=self.exitProgram)

		self.pack()

		#Add the area the plots will appear in
		self.f = Figure(figsize=(5,4), dpi=100)
		self.canvas=FigureCanvasTkAgg(self.f,master=root)
		self.canvas.show()
		self.canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
		toolbar = NavigationToolbar2TkAgg( self.canvas, root )
		toolbar.update()
		self.canvas._tkcanvas.pack(side="top", fill="both", expand=1)
		self.a = self.f.add_subplot(111)	

	
		#
		#Add buttons, text fields, and labels
		#
		xRangeLabel=Label(root,text="X Range:")
		xRangeLabel.pack(side="left")
		self.xRangeMinText=Text(root, width=5, height=1)
		self.xRangeMinText.pack(side="left")	
		xRangeMaxText=Text(root, width=5, height=1)
		xRangeMaxText.pack(side="left")

		peakText=Text(root, width=3, height=1)
		peakText.pack(side="right")
		peakLabel=Label(root,text="Peak:")
		peakLabel.pack(side="right")

		heightLabel=Label(root,text="Height:")
		heightLabel.pack(side="left")
		heightText=Text(master,width=6,height=1)
		heightText.pack(side="left")

		meanLabel=Label(root,text="Mean:")
		meanLabel.pack(side="left")
		meanText=Text(root,width=6,height=1)
		meanText.pack(side="left")

		widthLabel=Label(root,text="Width:")
		widthLabel.pack(side="left")
		widthText=Text(root,width=6,height=1)
		widthText.pack(side="left")
	
		replotButton=Button(root, text="Replot", command=self.replot)
		replotButton.pack(side="right", padx=10)
	
		clearButton=Button(root,text="Clear Plot", command=self.clearPlot)
		clearButton.pack(side="right",padx=10,pady=5)
		
	def fileOpen(self):
		filename=askopenfilename(filetypes=[("Data Files","*.dat *.DAT")])
		data=np.loadtxt(filename)
		self.plotData(data)
		return data

	def about(self):
		tkMessageBox.showinfo("About", "Stuff about RXF Data Fit.") 
	def manual(self):
		tkMessageBox.showinfo("Manual","How to use this program.")  
	def exitProgram(self):
		root.destroy()

	def replot(self):
		print "Not really."
		print self.canvas.show()
	def clearPlot(self,event):
		print "not cleared."
	
	def plotData(self,data):
		self.a.plot(data,'r+')
		dataPlot = self.canvas	
		dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
		dataPlot._tkcanvas.pack(side="top", fill="both", expand=1)
		dataPlot.show()

	def getXmin(self):
		xmin = self.xRangeMinText.get(1.0, END)
		return xmin

	def getXmax(self):
		xmax=self.xRangeMaxText.get(1.0,END)
		return xmax
if __name__ == "__main__":
	root = Tk()
	app = App(root)
	root.mainloop()
