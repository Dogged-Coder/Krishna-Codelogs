import customtkinter as ctk

# App setup
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")  # green theme to match your vibe

app = ctk.CTk()
app.geometry("300x450")
app.title("Green Glow Calculator")
app.resizable(False, False)

expression = ""

# --- Display ---
display = ctk.CTkEntry(app, font=("Consolas", 22), justify="right", width=260, height=50)
display.place(x=20, y=20)
display.insert(0, "0")
display.configure(state="readonly")

# --- Logic ---
def update_display(value):
    global expression
    if display.get() == "0":
        expression = value
    else:
        expression += value
    display.configure(state="normal")
    display.delete(0, ctk.END)
    display.insert(0, expression)
    display.configure(state="readonly")

def clear():
    global expression
    expression = ""
    display.configure(state="normal")
    display.delete(0, ctk.END)
    display.insert(0, "0")
    display.configure(state="readonly")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display.configure(state="normal")
        display.delete(0, ctk.END)
        display.insert(0, result)
        display.configure(state="readonly")
        expression = result
    except:
        display.configure(state="normal")
        display.delete(0, ctk.END)
        display.insert(0, "Error")
        display.configure(state="readonly")
        expression = ""

# --- Buttons ---
buttons = [
    ("7", 20, 90), ("8", 90, 90), ("9", 160, 90), ("/", 230, 90),
    ("4", 20, 150), ("5", 90, 150), ("6", 160, 150), ("*", 230, 150),
    ("1", 20, 210), ("2", 90, 210), ("3", 160, 210), ("-", 230, 210),
    ("0", 20, 270), ("C", 90, 270), ("=", 160, 270), ("+", 230, 270),
]

for (text, x, y) in buttons:
    if text == "C":
        cmd = clear
    elif text == "=":
        cmd = calculate
    else:
        cmd = lambda val=text: update_display(val)

    ctk.CTkButton(
        app,
        text=text,
        command=cmd,
        width=60,
        height=50,
        corner_radius=10,
        fg_color="#b2f2bb",       # Light green
        hover_color="#69db7c",    # Darker green on hover
        border_width=2,
        border_color="#2b8a3e",
        text_color="black"
    ).place(x=x, y=y)

app.mainloop()
