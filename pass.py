import customtkinter as ctk
import string
import random
import pyperclip
from PIL import Image, ImageSequence
import pygame
import threading
import os
import math

# Configure theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Root window (entry screen)
root = ctk.CTk()
root.geometry("600x450")
root.title("Welcome")
root.resizable(False, False)

entry_frame = ctk.CTkFrame(root, corner_radius=20)
entry_frame.place(relx=0.5, rely=0.5, anchor="center")

welcome_label = ctk.CTkLabel(entry_frame, text="Welcome to Jungle Password Generator 🌿", font=("Segoe UI", 18, "bold"), text_color="#00ff88")
welcome_label.pack(pady=20)

entry_button = ctk.CTkButton(entry_frame, text="Launch Generator", width=200, height=40, corner_radius=20, fg_color="#222", hover_color="#00ff88")
entry_button.pack(pady=20)

# ---- Generator App (hidden initially) ----
app = ctk.CTk()
app.geometry("600x450")
app.title("Jungle Password Generator")
app.resizable(False, False)

# Load and animate background GIF using CTkImage
bg_gif = Image.open("background.gif")
frames = [ctk.CTkImage(light_image=frame.copy().convert("RGBA"), size=(600, 450))
          for frame in ImageSequence.Iterator(bg_gif)]

bg_label = ctk.CTkLabel(app, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.lower()  # Ensure background stays in the back

frame_index = 0

def update_bg():
    global frame_index
    frame = frames[frame_index]
    frame_index = (frame_index + 1) % len(frames)
    bg_label.configure(image=frame)
    app.after(100, update_bg)

# Jungle background audio (looped)
pygame.mixer.init()
jungle_sound = pygame.mixer.Sound("jungle_click.wav")
jungle_sound.play(loops=-1)

# Load animal sounds into list
animal_sounds = [pygame.mixer.Sound(os.path.join("animal_sounds", file))
                 for file in os.listdir("animal_sounds") if file.endswith(".wav")]

def play_random_animal_sound():
    if animal_sounds:
        random.choice(animal_sounds).play()

# State variables
password_var = ctk.StringVar(value="Click Generate")
length_var = ctk.IntVar(value=16)
use_upper = ctk.BooleanVar(value=True)
use_lower = ctk.BooleanVar(value=True)
use_digits = ctk.BooleanVar(value=True)
use_symbols = ctk.BooleanVar(value=True)
username_var = ctk.StringVar()
website_var = ctk.StringVar()
password_history = []

# Typing animation logic
def animate_password(password):
    password_var.set("")
    def type_char(index=0):
        if index < len(password):
            current = password_var.get()
            password_var.set(current + password[index])
            entry.update_idletasks()
            entry.update()
            app.after(50, lambda: type_char(index + 1))
    type_char()

# Password logic
def generate_password():
    play_random_animal_sound()
    pool = ""
    if use_upper.get(): pool += string.ascii_uppercase
    if use_lower.get(): pool += string.ascii_lowercase
    if use_digits.get(): pool += string.digits
    if use_symbols.get(): pool += string.punctuation

    if not pool:
        password_var.set("Select options")
        return

    password = ''.join(random.choices(pool, k=length_var.get()))
    animate_password(password)
    strength_label.configure(text=strength_check(password))
    crack_time_label.configure(text=estimate_crack_time(password))

    if password not in password_history:
        password_history.insert(0, password)
        if len(password_history) > 5:
            password_history.pop()
        update_history()

def strength_check(pwd):
    score = sum([
        any(c.islower() for c in pwd),
        any(c.isupper() for c in pwd),
        any(c.isdigit() for c in pwd),
        any(c in string.punctuation for c in pwd),
        len(pwd) >= 12
    ])
    return ["Weak", "Weak", "Moderate", "Strong", "Very Strong", "Ultra"][score]

def estimate_crack_time(pwd):
    charset = 0
    if any(c.islower() for c in pwd): charset += 26
    if any(c.isupper() for c in pwd): charset += 26
    if any(c.isdigit() for c in pwd): charset += 10
    if any(c in string.punctuation for c in pwd): charset += len(string.punctuation)
    guesses = math.pow(charset, len(pwd))
    guesses_per_second = 1e10
    seconds = guesses / guesses_per_second
    years = seconds / (60*60*24*365)
    if years < 1:
        return f"🔓 Crack Time: {int(seconds)}s"
    elif years < 100:
        return f"🔐 Crack Time: {int(years)}y"
    else:
        return "🛡️ Nearly Uncrackable"

def copy_password():
    play_random_animal_sound()
    pyperclip.copy(password_var.get())
    copy_btn.configure(text="✓ Copied")
    app.after(1500, lambda: copy_btn.configure(text="Copy"))

def update_history():
    for widget in history_frame.winfo_children():
        widget.destroy()
    for i, pwd in enumerate(password_history):
        btn = ctk.CTkButton(history_frame, text=pwd[:20]+"..." if len(pwd) > 20 else pwd, width=250,
                            command=lambda p=pwd: pyperclip.copy(p),
                            fg_color="#333", hover_color="#00ff88")
        btn.grid(row=i, column=0, padx=5, pady=2)

def launch_main():
    root.destroy()
    app.deiconify()
    update_bg()

entry_button.configure(command=launch_main)

# Main app widgets (start hidden)
app.withdraw()

# Title
title_label = ctk.CTkLabel(app, text="Jungle Password Generator 🌿", font=("Segoe UI", 20, "bold"), text_color="#00ff88")
title_label.place(x=20, y=10)

# Username and Website
username_entry = ctk.CTkEntry(app, placeholder_text="Username", textvariable=username_var, width=140, fg_color="#111", border_color="#00ff88", border_width=2)
username_entry.place(x=20, y=50)

website_entry = ctk.CTkEntry(app, placeholder_text="Website/App", textvariable=website_var, width=140, fg_color="#111", border_color="#00ff88", border_width=2)
website_entry.place(x=20, y=90)

# Entry and Buttons
entry = ctk.CTkEntry(app, textvariable=password_var, font=("Consolas", 14), width=300)
entry.place(x=270, y=40)

copy_btn = ctk.CTkButton(app, text="Copy", command=copy_password, corner_radius=20, width=80, fg_color="#222", hover_color="#00ff88")
copy_btn.place(x=400, y=80)

strength_label = ctk.CTkLabel(app, text="", font=("Segoe UI", 12), text_color="#00ff88")
strength_label.place(x=270, y=80)

crack_time_label = ctk.CTkLabel(app, text="", font=("Segoe UI", 12), text_color="#00ff88")
crack_time_label.place(x=270, y=105)

length_label = ctk.CTkLabel(app, text="Password Length", font=("Segoe UI", 12), text_color="#ffffff")
length_label.place(x=270, y=130)

length_slider = ctk.CTkSlider(app, from_=8, to=64, variable=length_var, width=200)
length_slider.place(x=270, y=160)

checkbox1 = ctk.CTkCheckBox(app, text="Uppercase", variable=use_upper, command=play_random_animal_sound)
checkbox1.place(x=270, y=190)

checkbox2 = ctk.CTkCheckBox(app, text="Lowercase", variable=use_lower, command=play_random_animal_sound)
checkbox2.place(x=270, y=220)

checkbox3 = ctk.CTkCheckBox(app, text="Digits", variable=use_digits, command=play_random_animal_sound)
checkbox3.place(x=270, y=250)

checkbox4 = ctk.CTkCheckBox(app, text="Symbols", variable=use_symbols, command=play_random_animal_sound)
checkbox4.place(x=270, y=280)

generate_btn = ctk.CTkButton(app, text="Generate Password", command=generate_password, corner_radius=20, width=180, fg_color="#222", hover_color="#00ff88")
generate_btn.place(x=270, y=320)

history_frame = ctk.CTkScrollableFrame(app, width=250, height=90)
history_frame.place(x=270, y=360)

root.mainloop()
