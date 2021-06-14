
from tkinter import *
from Timer import Timer
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

import math
import matplotlib.animation as animation

# GLOBAL DATA ARRAY
g_data = []

# Function Timer
timer = Timer()
timer.reset()
time_stamps = []

# Plotting Figure Variables
# the figure that will contain the plot
fig = Figure(figsize = (5, 5), dpi = 100)
# adding the subplot
ax1 = fig.add_subplot(111)

# data
data = []

# plot function is created for
# plotting the graph in
# tkinter window
def animate(i):

    time_stamps.append(timer.getCurrentTime())
    # list of squares
    data.append(math.sin(time_stamps[-1]*3)*time_stamps[-1]**2)
    # plotting the graph
    ax1.clear()
    ax1.plot(time_stamps, data)

# the main Tkinter window
window = Tk()

# Setup figure within the window
# creating the Tkinter canvas
# containing the Matplotlib figure
canvas = FigureCanvasTkAgg(fig, master = window)
canvas.draw()
# placing the canvas on the Tkinter window
canvas.get_tk_widget().pack()
# creating the Matplotlib toolbar
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()
# placing the toolbar on the Tkinter window
canvas.get_tk_widget().pack()

ani = animation.FuncAnimation(fig, animate, interval=50)

# setting the title
window.title('Plotting in Tkinter')
# dimensions of the main window
window.geometry("500x500")
# run the gui
window.mainloop()
