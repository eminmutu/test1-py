import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

period = 1e-3
t = np.linspace(0, 5*period, 1000)
v = ( (t % period) < (0.5e-3) ).astype(float)

fig, ax = plt.subplots(figsize=(6,3))
ax.step(t*1e3, v, where='post')
ax.set_xlabel("Time (ms)")
ax.set_ylabel("Voltage (V)")
ax.set_ylim(-0.2, 1.2)

root = tk.Tk()
root.title("Pulse Waveform (matplotlib)")
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
canvas.draw()
root.mainloop()