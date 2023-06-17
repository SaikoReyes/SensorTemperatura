import tkinter as tk
from tkinter import ttk
import serial
import time

# Open the serial port
ser = serial.Serial('/dev/cu.usbmodem1301', 9600)

def update_progress_bar():
  # Read the value from the serial port
  line = ser.readline()
  value = int(line)

  # Update the progress bar
  progress['value'] = value
  print("hola")
  print(value)
  # Schedule the next update
  root.after(1000, update_progress_bar)

# Create the main window
root = tk.Tk()

# Create the progress bar
progress = tk.ttk.Progressbar(root, length=400, mode='determinate', maximum=255)
progress.pack()

# Start the update loop
root.after(1000, update_progress_bar)

# Start the main loop
root.mainloop()
