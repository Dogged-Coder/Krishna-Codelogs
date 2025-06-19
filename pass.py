import tkinter as tk
from tkinter import messagebox
import string
import random
import pyperclip
from PIL import Image, ImageTk, ImageSequence

root = tk.Tk()
root.title("🔥 Sexy Animated Password Generator")
root.geometry("500x650")
root.configure(bg="#1e1e2e")

# ------------ Animated GIF Class ------------
class AnimatedGIF(tk.Label):
    def __init__(self, master, path, delay=100):
        super().__init__(master, bg="#1e1e2e")
        self.master = master
        self.delay = delay
        self.frames = []
        self.idx = 0

        pil_img = Image.open(path)
        for frame in ImageSequence.Iterator(pil_img):
            frame = frame.resize((60, 60))  # Resize to button size
            self.frames.append(ImageTk.PhotoImage(frame))

        self.config(image=self.frames[0])
        self.animate()

    def animate(self):
        self.config(image=self.frames[self.idx])
        self.idx = (self.idx + 1) % len(self.frames)
        self.after(self.delay, self.animate)

# ------------ Password Logic ------------
def generate_password():
    length = length_var.get()
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digit_var.get()
    use_symbols = symbol_var.get()

    min_upper = min_upper_var.get()
    min_lower = min_lower_var.get()
    min_digits = min_digit_var.get()
    min_symbols = min_symbol_var.get()

    if length < (min_upper + min_lower + min_digits + min_symbols):
        messagebox.showerror("Too Short", "Increase password length.")
        return

    chars = []
    chars += random.choices(string.ascii_uppercase, k=min_upper)
    chars += random.choices(string.ascii_lowercase, k=min_lower)
    chars += random.choices(string.digits, k=min_digits)
    chars += random.choices(string.punctuation, k=min_symbols)

    pool = ""
    if use_upper: pool += string.ascii_uppercase
    if use_lower: pool += string.ascii_lowercase
    if use_digits: pool += string.digits
    if use_symbols: pool += string.punctuation

    remaining = length - len(chars)
    chars += random.choices(pool, k=remaining)
    random.shuffle(chars)

    password = ''.join(chars)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied!", "Password copied to clipboard.")
    else:
        messagebox.showwarning("Empty", "No password to copy.")

# ------------ UI Setup ------------
tk.Label(root, text="🌀 Animated Password Forge", font=("Impact", 18), fg="#89b4fa", bg="#1e1e2e").pack(pady=20)

password_entry = tk.Entry(root, font=("Consolas", 16), width=30, justify='center', bd=3, bg="#2e2e38", fg="#00f5ff", insertbackground="#00f5ff")
password_entry.pack(pady=10, ipady=10)

# Animated Copy Button
copy_gif = AnimatedGIF(root, "copy.gif")
copy_gif.bind("<Button-1>", lambda e: copy_password())
copy_gif.pack(pady=10)

# Length slider
tk.Label(root, text="Length", font=("Segoe UI", 12), fg="#fff", bg="#1e1e2e").pack()
length_var = tk.IntVar(value=16)
tk.Scale(root, from_=8, to=64, variable=length_var, orient=tk.HORIZONTAL, length=300,
         bg="#1e1e2e", fg="#00ffcc", troughcolor="#444", highlightthickness=0).pack()

# Checkboxes
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

for text, var in [("Uppercase", upper_var), ("Lowercase", lower_var),
                  ("Digits", digit_var), ("Symbols", symbol_var)]:
    tk.Checkbutton(root, text=text, variable=var, font=("Segoe UI", 11),
                   bg="#1e1e2e", fg="white", selectcolor="#444").pack(anchor='w', padx=100)

# Minimum required fields
tk.Label(root, text="Minimums", font=("Segoe UI", 12), fg="#fff", bg="#1e1e2e").pack(pady=10)
frame = tk.Frame(root, bg="#1e1e2e")
frame.pack()

min_upper_var = tk.IntVar(value=1)
min_lower_var = tk.IntVar(value=1)
min_digit_var = tk.IntVar(value=1)
min_symbol_var = tk.IntVar(value=1)

for i, (label, var) in enumerate([("Upper", min_upper_var), ("Lower", min_lower_var),
                                  ("Digits", min_digit_var), ("Symbols", min_symbol_var)]):
    tk.Label(frame, text=label, font=("Segoe UI", 11), fg="white", bg="#1e1e2e").grid(row=i, column=0, padx=5, pady=3)
    tk.Entry(frame, textvariable=var, width=5).grid(row=i, column=1, padx=5)

# Animated Generate Button
generate_gif = AnimatedGIF(root, "generate.gif")
generate_gif.bind("<Button-1>", lambda e: generate_password())
generate_gif.pack(pady=20)

root.mainloop()
