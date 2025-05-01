import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

# Membership Function Definitions
def triangular_mf(x, a, b, c):
    return np.maximum(np.minimum((x - a)/(b - a), (c - x)/(c - b)), 0)

def trapezoidal_mf(x, a, b, c, d):
    return np.maximum(np.minimum(np.minimum((x - a)/(b - a), 1), (d - x)/(d - c)), 0)

def gaussian_mf(x, c, sigma):
    return np.exp(-0.5 * ((x - c)/sigma) ** 2)

def sigmoid_mf(x, a, c):
    return 1 / (1 + np.exp(-a * (x - c)))

# Plot Functions
def plot_triangular():
    x = np.linspace(0, 10, 100)
    y = triangular_mf(x, 2, 5, 8)
    plt.plot(x, y)
    plt.title('Triangular Membership Function')
    plt.xlabel('x')
    plt.ylabel('Membership')
    plt.grid(True)
    plt.show()

def plot_trapezoidal():
    x = np.linspace(0, 10, 100)
    y = trapezoidal_mf(x, 2, 4, 6, 8)
    plt.plot(x, y)
    plt.title('Trapezoidal Membership Function')
    plt.xlabel('x')
    plt.ylabel('Membership')
    plt.grid(True)
    plt.show()

def plot_gaussian():
    x = np.linspace(0, 10, 100)
    y = gaussian_mf(x, c=5, sigma=1.5)
    plt.plot(x, y)
    plt.title('Gaussian Membership Function')
    plt.xlabel('x')
    plt.ylabel('Membership')
    plt.grid(True)
    plt.show()

def plot_sigmoid():
    x = np.linspace(0, 10, 100)
    y = sigmoid_mf(x, a=1, c=5)
    plt.plot(x, y)
    plt.title('Sigmoid Membership Function')
    plt.xlabel('x')
    plt.ylabel('Membership')
    plt.grid(True)
    plt.show()

# GUI Code
root = tk.Tk()
root.title("Fuzzy Membership Function Plotter")
root.geometry("400x300")

ttk.Label(root, text="Select Membership Function to Plot", font=('Arial', 14)).pack(pady=10)

ttk.Button(root, text="Triangular", command=plot_triangular).pack(pady=5)
ttk.Button(root, text="Trapezoidal", command=plot_trapezoidal).pack(pady=5)
ttk.Button(root, text="Gaussian", command=plot_gaussian).pack(pady=5)
ttk.Button(root, text="Sigmoid", command=plot_sigmoid).pack(pady=5)

root.mainloop()
