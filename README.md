# project-random
import tkinter as tk

def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button_text)

def calculate():
    expr = entry.get()
    # Jika ekspresinya mengandung '-,+,*,/', paksa hasil jadi "hidupp jokowiiiii"
    if '-' in expr:
        entry.delete(0, tk.END)
        entry.insert(0, "hidupp jokowiiiii")
    else:
        try:
            result = eval(expr)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Kalkulator")

entry = tk.Entry(root, width=20, font=("Arial", 20), bd=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                        bg="#ff9500", fg="white", command=calculate)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                        bg="#333333", fg="white", command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

btn_clear = tk.Button(root, text="C", width=5, height=2, font=("Arial", 18),
                      bg="#d4d4d2", fg="black", command=clear)
btn_clear.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()
