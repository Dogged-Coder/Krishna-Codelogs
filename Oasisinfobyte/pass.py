import customtkinter as ctk
import string
import random
import pyperclip
from PIL import Image, ImageTk, ImageSequence
import pygame
import threading

# Configure theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# App window
app = ctk.CTk()
app.geometry("600x360")
app.title("Jungle Password Generator")
app.resizable(False, False)

# Load and animate background GIF
frames = []
bg_gif = Image.open("background.gif")
for frame in ImageSequence.Iterator(bg_gif):
    frame = frame.resize((600, 360))
    frames.append(ImageTk.PhotoImage(frame))

bg_label = ctk.CTkLabel(app, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

frame_index = 0

def update_bg():
    global frame_index
    frame = frames[frame_index]
    frame_index = (frame_index + 1) % len(frames)
    bg_label.configure(image=frame)
    app.after(100, update_bg)

update_bg()

# Jungle background audio (looped)
pygame.mixer.init()
jungle_sound = pygame.mixer.Sound("jungle_click.wav")
jungle_sound.play(loops=-1)

# State variables
password_var = ctk.StringVar(value="Click Generate")
length_var = ctk.IntVar(value=16)
use_upper = ctk.BooleanVar(value=True)
use_lower = ctk.BooleanVar(value=True)
use_digits = ctk.BooleanVar(value=True)
use_symbols = ctk.BooleanVar(value=True)

# Password logic
def generate_password():
    pool = ""
    if use_upper.get(): pool += string.ascii_uppercase
    if use_lower.get(): pool += string.ascii_lowercase
    if use_digits.get(): pool += string.digits
    if use_symbols.get(): pool += string.punctuation

    if not pool:
        password_var.set("Select options")
        return

    password = ''.join(random.choices(pool, k=length_var.get()))
    password_var.set(password)
    strength_label.configure(text=strength_check(password))

def strength_check(pwd):
    score = sum([
        any(c.islower() for c in pwd),
        any(c.isupper() for c in pwd),
        any(c.isdigit() for c in pwd),
        any(c in string.punctuation for c in pwd),
        len(pwd) >= 12
    ])
    return ["Weak", "Weak", "Moderate", "Strong", "Very Strong", "Ultra"][score]

def copy_password():
    pyperclip.copy(password_var.get())
    copy_btn.configure(text="✓ Copied")
    app.after(1500, lambda: copy_btn.configure(text="Copy"))

# Title (Moved to top left corner to not block the character or waterfall)
title_label = ctk.CTkLabel(app, text="Jungle Password Generator 🌿", font=("Segoe UI", 20, "bold"), text_color="#00ff88")
title_label.place(x=20, y=10)

# Entry and Buttons (positioned right side to avoid character & waterfall)
entry = ctk.CTkEntry(app, textvariable=password_var, font=("Consolas", 14), width=300)
entry.place(x=270, y=40)

copy_btn = ctk.CTkButton(app, text="Copy", command=copy_password, corner_radius=20, width=80)
copy_btn.place(x=400, y=80)

strength_label = ctk.CTkLabel(app, text="", font=("Segoe UI", 12), text_color="#00ff88")
strength_label.place(x=270, y=80)

length_label = ctk.CTkLabel(app, text="Password Length", font=("Segoe UI", 12), text_color="#ffffff")
length_label.place(x=270, y=120)

length_slider = ctk.CTkSlider(app, from_=8, to=64, variable=length_var, width=200)
length_slider.place(x=270, y=150)

# Checkboxes vertically stacked right side
ctk.CTkCheckBox(app, text="Uppercase", variable=use_upper).place(x=270, y=190)
ctk.CTkCheckBox(app, text="Lowercase", variable=use_lower).place(x=270, y=220)
ctk.CTkCheckBox(app, text="Digits", variable=use_digits).place(x=270, y=250)
ctk.CTkCheckBox(app, text="Symbols", variable=use_symbols).place(x=270, y=280)

# Generate button (bottom right)
ctk.CTkButton(app, text="Generate Password", command=generate_password, corner_radius=20, width=180).place(x=270, y=310)

app.mainloop()
