import customtkinter as ctk
from tkinter import Canvas, PhotoImage
from PIL import Image, ImageTk, ImageSequence

# App Setup
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("450x600")
app.title("GIF Styled Calculator")
app.resizable(False, False)

# Canvas for GIF Background
canvas = Canvas(app, width=450, height=450, highlightthickness=0)
canvas.place(x=0, y=0)

# Load GIF frames using PIL
gif = Image.open("back.gif")
gif_frames = [ImageTk.PhotoImage(frame.copy().resize((450, 450))) for frame in ImageSequence.Iterator(gif)]
frame_index = 0

def animate():
    global frame_index
    canvas.create_image(0, 0, anchor="nw", image=gif_frames[frame_index])
    frame_index = (frame_index + 1) % len(gif_frames)
    app.after(100, animate)

animate()

# --- Cover the Digital Display Area on GIF ---
cover = ctk.CTkFrame(app, width=190, height=60, fg_color="white")
cover.place(x=130, y=30)

# --- Calculator Display ---
current_expression = ""
entry = ctk.CTkEntry(app, font=("Consolas", 20), justify="right", width=180)
entry.place(x=135, y=40)
entry.insert(0, "0")
entry.configure(state="readonly")

# --- Calculator Logic ---
def press(value):
    global current_expression
    if entry.get() == "0":
        current_expression = value
    else:
        current_expression += value
    entry.configure(state="normal")
    entry.delete(0, ctk.END)
    entry.insert(0, current_expression)
    entry.configure(state="readonly")

def clear():
    global current_expression
    current_expression = ""
    entry.configure(state="normal")
    entry.delete(0, ctk.END)
    entry.insert(0, "0")
    entry.configure(state="readonly")

def calculate():
    global current_expression
    try:
        result = str(eval(current_expression))
        entry.configure(state="normal")
        entry.delete(0, ctk.END)
        entry.insert(0, result)
        entry.configure(state="readonly")
        current_expression = result
    except:
        entry.configure(state="normal")
        entry.delete(0, ctk.END)
        entry.insert(0, "Error")
        entry.configure(state="readonly")
        current_expression = ""

# --- Buttons Below the GIF (same layout as shown in gif) ---
button_cfg = dict(width=80, height=50, corner_radius=10, fg_color="#eeeeee", hover_color="#cccccc")

x_start, y_start = 50, 470
spacing_x, spacing_y = 90, 60

buttons = [
    ("7", x_start, y_start),
    ("8", x_start + spacing_x, y_start),
    ("9", x_start + 2*spacing_x, y_start),

    ("4", x_start, y_start + spacing_y),
    ("5", x_start + spacing_x, y_start + spacing_y),
    ("6", x_start + 2*spacing_x, y_start + spacing_y),

    ("1", x_start, y_start + 2*spacing_y),
    ("2", x_start + spacing_x, y_start + 2*spacing_y),
    ("3", x_start + 2*spacing_x, y_start + 2*spacing_y),

    ("0", x_start, y_start + 3*spacing_y),
    ("C", x_start + spacing_x, y_start + 3*spacing_y),
    ("=", x_start + 2*spacing_x, y_start + 3*spacing_y),
]

for txt, x, y in buttons:
    if txt == "C":
        cmd = clear
    elif txt == "=":
        cmd = calculate
    else:
        cmd = lambda val=txt: press(val)
    ctk.CTkButton(app, text=txt, command=cmd, **button_cfg).place(x=x, y=y)

app.mainloop()
