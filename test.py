import Tkinter

class SimplePlot(Tkinter.Canvas):

    def plot(self, x, y):
        self.create_line((x, y, x+1, y), fill="black")
import random, time


root = Tkinter.Tk()
root.title("demoSimplePlot")

widget = SimplePlot(root)
widget.pack(fill="both", expand=1)

widget.update() # display the widget

data = []
for i in range(5000):
    data.append((random.randint(0, 200), random.randint(0, 200)))

t0 = time.time()

for x, y in data:
    widget.plot(x, y)

widget.update() # make sure everything is drawn

print time.time() - t0, "seconds"

root.mainloop()
