import numpy as np
import pylab as pl

for i in data:
	xnew=[j]
	x=x+xnew
	j=j+1
pl.plot(x,data, 'ro')
pl.title(filename)
pl.xlabel("ADC Counts")
pl.ylabel("Occurences")
pl.show()
