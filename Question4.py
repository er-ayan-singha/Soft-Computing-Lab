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

def complement(fset):
    return {x: round(1 - mu, 2) for x, mu in fset.items()}

def union(A, B):
    return {x: max(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

def intersection(A, B):
    return {x: min(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

def de_morgan():
    A = parse_fuzzy_set(entry_setA.get())
    B = parse_fuzzy_set(entry_setB.get())
    if not A or not B:
        return

    A_comp = complement(A)
    B_comp = complement(B)

    union_AB = union(A, B)
    inter_AB = intersection(A, B)

    demorgan1_lhs = complement(union_AB)
    demorgan1_rhs = intersection(A_comp, B_comp)

    demorgan2_lhs = complement(inter_AB)
    demorgan2_rhs = union(A_comp, B_comp)

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, f"A: {A}\nB: {B}\n\n")
    text_output.insert(tk.END, f"A': {A_comp}\nB': {B_comp}\n\n")

    text_output.insert(tk.END, "De Morgan's Law 1:\n")
    text_output.insert(tk.END, f"(A ∪ B)' = {demorgan1_lhs}\n")
    text_output.insert(tk.END, f"A' ∩ B' = {demorgan1_rhs}\n\n")

    text_output.insert(tk.END, "De Morgan's Law 2:\n")
    text_output.insert(tk.END, f"(A ∩ B)' = {demorgan2_lhs}\n")
    text_output.insert(tk.END, f"A' ∪ B' = {demorgan2_rhs}\n\n")

    if demorgan1_lhs == demorgan1_rhs and demorgan2_lhs == demorgan2_rhs:
        text_output.insert(tk.END, "✅ De Morgan's Laws verified successfully.")
    else:
        text_output.insert(tk.END, "❌ De Morgan's Laws do not hold (check input).")

def generate_random_sets():
    elements = ['x1', 'x2', 'x3', 'x4']
    A = ",".join([f"{el}:{round(random.uniform(0, 1), 2)}" for el in elements])
    B = ",".join([f"{el}:{round(random.uniform(0, 1), 2)}" for el in elements])
    entry_setA.delete(0, tk.END)
    entry_setB.delete(0, tk.END)
    entry_setA.insert(0, A)
    entry_setB.insert(0, B)

# GUI Setup
root = tk.Tk()
root.title("De Morgan's Law in Fuzzy Logic")

tk.Label(root, text="Enter Fuzzy Set A (e.g., x1:0.3,x2:0.6):").pack()
entry_setA = tk.Entry(root, width=60)
entry_setA.pack()

tk.Label(root, text="Enter Fuzzy Set B (e.g., x1:0.5,x2:0.8):").pack()
entry_setB = tk.Entry(root, width=60)
entry_setB.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Verify De Morgan’s Laws", command=de_morgan).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Generate Random Sets", command=generate_random_sets).pack(side=tk.LEFT, padx=5)

text_output = tk.Text(root, height=20, width=80)
text_output.pack()

root.mainloop()
