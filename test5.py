# Simple Tkinter GUI example
import tkinter as tk

# Parameters for the pulse waveform
period_ms = 1.0      # total period in milliseconds
high_ms = 0.5        # high duration (1 V)
low_ms = 0.5         # low duration (0 V)
num_periods = 5      # how many periods to display
high_voltage = 1.0
low_voltage = 0.0

total_time_ms = num_periods * period_ms

root = tk.Tk()
root.title("Pulse Waveform (Square Wave)")

width, height = 700, 300
margin = 40

canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()

# Axes
canvas.create_line(margin, height - margin, width - margin, height - margin, width=2)  # X axis
canvas.create_line(margin, margin, margin, height - margin, width=2)                  # Y axis
canvas.create_text(width // 2, height - 10, text="Time (ms)")
canvas.create_text(15, height // 2, text="V", angle=90)

# Ticks for voltage (0 V and 1 V)
for v in (0.0, 1.0):
    y = height - margin - v * (height - 2 * margin)
    canvas.create_line(margin - 6, y, margin, y, width=2)
    canvas.create_text(margin - 20, y, text=f"{v:.0f}V")

# Time ticks (each ms)
for p in range(num_periods + 1):
    t_ms = p * period_ms
    x = margin + (t_ms / total_time_ms) * (width - 2 * margin)
    canvas.create_line(x, height - margin, x, height - margin + 6, width=2)
    canvas.create_text(x, height - margin + 18, text=f"{t_ms:.0f}")

# Generate pulse points
points = []
current_time = 0.0
for n in range(num_periods):
    t0 = n * period_ms
    # High segment
    points.append((t0, high_voltage))
    points.append((t0 + high_ms, high_voltage))
    # Low segment
    points.append((t0 + high_ms, low_voltage))
    points.append((t0 + period_ms, low_voltage))

# Convert to canvas coordinates and draw
def to_canvas(t_ms, v):
    x = margin + (t_ms / total_time_ms) * (width - 2 * margin)
    y = height - margin - v * (height - 2 * margin)
    return x, y

# Draw waveform
for i in range(len(points) - 1):
    x1, y1 = to_canvas(*points[i])
    x2, y2 = to_canvas(*points[i + 1])
    canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

# Legend
canvas.create_rectangle(width - 180, margin, width - 30, margin + 50, outline="black")
canvas.create_line(width - 170, margin + 15, width - 140, margin + 15, fill="blue", width=2)
canvas.create_text(width - 100, margin + 15, text="Pulse 1 kHz")
canvas.create_text(width - 105, margin + 35, text="0.5 ms @1V / 0.5 ms @0V")

root.mainloop()