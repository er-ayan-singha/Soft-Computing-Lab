import tkinter as tk
from tkinter import messagebox, filedialog
import numpy as np

# ======== Functions ========= #
def parse_array(input_text):
    try:
        arr = np.array([float(i.strip()) for i in input_text.split(',')])
        return arr
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numbers separated by commas.")
        return None

def array_operations(arr):
    return {
        "Sum": np.sum(arr),
        "Mean": np.mean(arr),
        "Max": np.max(arr),
        "Min": np.min(arr),
        "Sorted": np.sort(arr),
        "Shape": arr.shape
    }

def display_results(results):
    output_text.delete('1.0', tk.END)
    for key, val in results.items():
        output_text.insert(tk.END, f"{key}: {val}\n")

def perform_operations():
    arr_text = entry.get()
    arr = parse_array(arr_text)
    if arr is not None:
        results = array_operations(arr)
        display_results(results)

def save_to_file():
    content = output_text.get('1.0', tk.END)
    if content.strip() == "":
        messagebox.showwarning("No Data", "There is no data to save.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(content)
        messagebox.showinfo("Saved", f"Results saved to {file_path}")

def clear_all():
    entry.delete(0, tk.END)
    output_text.delete('1.0', tk.END)

def load_demo_array(arr):
    entry.delete(0, tk.END)
    entry.insert(0, ", ".join(map(str, arr)))

# ======== GUI Setup ========= #
root = tk.Tk()
root.title("Array Operations Tool")
root.geometry("500x500")

tk.Label(root, text="Enter array (comma-separated):").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Demo buttons
demo_frame = tk.Frame(root)
tk.Label(demo_frame, text="Demo Arrays:").pack(side=tk.LEFT, padx=5)
tk.Button(demo_frame, text="[1, 2, 3, 4, 5]", command=lambda: load_demo_array([1, 2, 3, 4, 5])).pack(side=tk.LEFT)
tk.Button(demo_frame, text="[10, 20, 30, 40]", command=lambda: load_demo_array([10, 20, 30, 40])).pack(side=tk.LEFT)
tk.Button(demo_frame, text="[5.5, 2.2, 9.1]", command=lambda: load_demo_array([5.5, 2.2, 9.1])).pack(side=tk.LEFT)
demo_frame.pack(pady=5)

# Action buttons
tk.Button(root, text="Perform Operations", command=perform_operations).pack(pady=5)
tk.Button(root, text="Save to File", command=save_to_file).pack(pady=5)
tk.Button(root, text="Clear", command=clear_all).pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

# Output field
output_text = tk.Text(root, height=10, width=60)
output_text.pack(pady=10)

root.mainloop()
