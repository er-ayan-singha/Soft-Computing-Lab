import tkinter as tk
from tkinter import messagebox
import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import random

# Colors
colors = ['red', 'blue', 'green', 'yellow', 'black', 'magenta', 'cyan', 'orange', 'purple', 'brown']
color_vars = {}

# Ensure only one color is selected at a time
def select_only_this(selected_color):
    for color, var in color_vars.items():
        var.set(1 if color == selected_color else 0)

def get_selected_color():
    for color, var in color_vars.items():
        if var.get() == 1:
            return color
    return 'blue'  # fallback default

# Generate sine wave
def generate_sine_wave(freq, sampling_rate, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    y = np.sin(2 * np.pi * freq * t)
    return t, y

# Plot signal
def plot_signal(t, y, color):
    plt.figure(figsize=(8, 4))
    plt.plot(t, y, color=color)
    plt.title(f"Sine Wave - {color}")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Plot FFT
def perform_fft(y, sampling_rate, color):
    N = len(y)
    yf = fft(y)
    xf = fftfreq(N, 1 / sampling_rate)
    plt.figure(figsize=(8, 4))
    plt.plot(xf[:N // 2], np.abs(yf[:N // 2]), color=color)
    plt.title("FFT (Frequency Domain)")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Main handler
def generate_and_plot():
    try:
        freq = float(entry_freq.get())
        rate = float(entry_rate.get())
        dur = float(entry_dur.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
        return

    selected_color = get_selected_color()
    t, y = generate_sine_wave(freq, rate, dur)
    plot_signal(t, y, selected_color)
    perform_fft(y, rate, selected_color)  # Pass color here

# Generate random input values
def generate_random_input():
    # Random values within some typical ranges
    random_freq = random.uniform(1, 20)  # Random frequency between 1 and 20 Hz
    random_rate = random.randint(50, 500)  # Random sampling rate between 50 and 500 Hz
    random_dur = random.uniform(0.5, 5)  # Random duration between 0.5 and 5 seconds

    # Set random values into the entry fields
    entry_freq.delete(0, tk.END)
    entry_freq.insert(0, f"{random_freq:.2f}")

    entry_rate.delete(0, tk.END)
    entry_rate.insert(0, f"{random_rate}")

    entry_dur.delete(0, tk.END)
    entry_dur.insert(0, f"{random_dur:.2f}")

# GUI Setup
root = tk.Tk()
root.title("Sine Wave Generator with Color Checkboxes")
root.geometry("420x600")

# Input Fields
tk.Label(root, text="Frequency (Hz):").pack(pady=5)
entry_freq = tk.Entry(root)
entry_freq.insert(0, "5")
entry_freq.pack()

tk.Label(root, text="Sampling Rate (Hz):").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.insert(0, "100")
entry_rate.pack()

tk.Label(root, text="Duration (s):").pack(pady=5)
entry_dur = tk.Entry(root)
entry_dur.insert(0, "2")
entry_dur.pack()

# Color Selection
tk.Label(root, text="Select Plot Color:").pack(pady=10)
color_frame = tk.Frame(root)
color_frame.pack()

# Fix lambda using factory function
def make_checkbutton(color):
    var = tk.IntVar(value=1 if color == 'blue' else 0)
    chk = tk.Checkbutton(color_frame, text=color.title(), variable=var,
                         command=lambda: select_only_this(color))
    return var, chk

for i, color in enumerate(colors):
    var, chk = make_checkbutton(color)
    chk.grid(row=i // 2, column=i % 2, sticky='w', padx=10, pady=2)
    color_vars[color] = var

# Buttons
tk.Button(root, text="Generate & Plot", command=generate_and_plot).pack(pady=15)
tk.Button(root, text="Generate Random Input", command=generate_random_input).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

root.mainloop()
