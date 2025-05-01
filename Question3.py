import tkinter as tk
from tkinter import messagebox
import random

def parse_fuzzy_set(input_str):
    try:
        elements = input_str.split(",")
        fuzzy_set = {}
        for element in elements:
            x, mu = element.split(":")
            fuzzy_set[x.strip()] = float(mu.strip())
        return fuzzy_set
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input format: {e}")
        return {}

def fuzzy_sum(A, B):
    return {x: min(1, A.get(x, 0) + B.get(x, 0)) for x in set(A) | set(B)}

def fuzzy_subtraction(A, B):
    return {x: max(0, A.get(x, 0) - B.get(x, 0)) for x in set(A) | set(B)}

def fuzzy_product(A, B):
    return {x: round(A.get(x, 0) * B.get(x, 0), 2) for x in set(A) | set(B)}

def perform_operations():
    setA = parse_fuzzy_set(entry_setA.get())
    setB = parse_fuzzy_set(entry_setB.get())

    sum_result = fuzzy_sum(setA, setB)
    subtract_result = fuzzy_subtraction(setA, setB)
    product_result = fuzzy_product(setA, setB)

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, f"Set A: {setA}\n")
    text_output.insert(tk.END, f"Set B: {setB}\n\n")
    text_output.insert(tk.END, f"Sum (A + B): {sum_result}\n")
    text_output.insert(tk.END, f"Subtraction (A - B): {subtract_result}\n")
    text_output.insert(tk.END, f"Product (A * B): {product_result}\n")

def generate_random_sets():
    elements = ['x1', 'x2', 'x3', 'x4', 'x5']
    setA = ",".join([f"{el}:{round(random.uniform(0, 1), 2)}" for el in elements])
    setB = ",".join([f"{el}:{round(random.uniform(0, 1), 2)}" for el in elements])
    entry_setA.delete(0, tk.END)
    entry_setB.delete(0, tk.END)
    entry_setA.insert(0, setA)
    entry_setB.insert(0, setB)

# GUI setup
root = tk.Tk()
root.title("Fuzzy Set Arithmetic Operations")

tk.Label(root, text="Enter Set A (format: x1:mu1,x2:mu2,...):").pack()
entry_setA = tk.Entry(root, width=50)
entry_setA.pack()

tk.Label(root, text="Enter Set B (format: x1:mu1,x2:mu2,...):").pack()
entry_setB = tk.Entry(root, width=50)
entry_setB.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Compute", command=perform_operations).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Random Sets", command=generate_random_sets).pack(side=tk.LEFT, padx=5)

text_output = tk.Text(root, height=15, width=70)
text_output.pack()

root.mainloop()
