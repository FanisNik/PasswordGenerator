import random
import tkinter as tk
from tkinter import messagebox
import pyperclip

UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"
SYMBOLS = ".,!@#$%^&*()"
ALL_CHARACTERS = UPPERCASE + LOWERCASE + NUMBERS + SYMBOLS

class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, cornerradius, padding, color, text='', command=None):
        tk.Canvas.__init__(self, parent, width=width, height=height, highlightthickness=0, bg=parent["bg"])
        self.command = command
        self.color = color  

        if cornerradius > 0.5 * min(width, height):
            cornerradius = 0.5 * min(width, height)

        self.rect = self.round_rectangle(padding, padding, width-padding, height-padding, 
                                         cornerradius, fill=color)
        self.text = self.create_text(width/2, height/2, text=text, fill='white', font=('SF Pro Display', 12))

        self.bind('<ButtonPress-1>', self.on_press)
        self.bind('<ButtonRelease-1>', self.on_release)

    def round_rectangle(self, x1, y1, x2, y2, radius, **kwargs):
        points = [x1+radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1]
        return self.create_polygon(points, smooth=True, **kwargs)

    def on_press(self, event):
        self.itemconfig(self.rect, fill='gray')

    def on_release(self, event):
        self.itemconfig(self.rect, fill=self.color)
        if self.command:
            self.command()

def generate_password(length):
    length = max(4, length)  # Ensures the password length is at least 4
    password = [random.choice(UPPERCASE), random.choice(LOWERCASE),
                random.choice(NUMBERS), random.choice(SYMBOLS)]
    password += random.choices(ALL_CHARACTERS, k=length-4)
    random.shuffle(password)
    return ''.join(password)

def on_generate():
    try:
        length = int(length_entry.get())
        
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return
        elif length > 25:
            messagebox.showerror("Error", "Password length cannot be greater than 25.")
            return
        
        generated_password = generate_password(length)
        result_label.config(text=generated_password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def copy_password():
    password = result_label.cget("text")
    if password.strip():  
        pyperclip.copy(password)
    else:
        messagebox.showerror("Error", "No password to copy!")

BACKGROUND_COLOR = "#F2F2F7"  
BUTTON_COLOR = "#007AFF"      
TEXT_COLOR = "#000000"        

app = tk.Tk()
app.title("Password Generator")
app.configure(bg=BACKGROUND_COLOR)
app.geometry("300x450")

main_frame = tk.Frame(app, bg=BACKGROUND_COLOR, padx=20, pady=20)
main_frame.pack(expand=True, fill='both')

title_label = tk.Label(
    main_frame,
    text="Password Generator",
    font=('SF Pro Display', 24, 'bold'),
    bg=BACKGROUND_COLOR,
    fg=TEXT_COLOR
)
title_label.pack(pady=(0, 20))

length_label = tk.Label(
    main_frame,
    text="Password Length",
    font=('SF Pro Display', 14),
    bg=BACKGROUND_COLOR,
    fg=TEXT_COLOR
)
length_label.pack(pady=(0, 5))

length_entry = tk.Entry(
    main_frame,
    font=('SF Pro Display', 14),
    justify='center',
    width=10,
    validate='key',
)
length_entry.pack(pady=(0, 20))
length_entry.insert(0, "12")  

generate_button = RoundedButton(
    main_frame,
    width=200,
    height=40,
    cornerradius=20,
    padding=0,
    color=BUTTON_COLOR,
    text="Generate Password",
    command=on_generate
)
generate_button.pack(pady=20)

result_frame = tk.Frame(main_frame, bg='white', padx=15, pady=15)
result_frame.pack(fill='x', pady=20)

result_label = tk.Label(
    result_frame,
    text="Password will appear here",
    font=('SF Pro Display', 12),
    bg='white',
    fg=TEXT_COLOR
)
result_label.pack()

copy_button = RoundedButton(
    main_frame,
    width=200,
    height=40,
    cornerradius=20,  
    padding=0,
    color=BUTTON_COLOR,
    text="Copy Password",
    command=copy_password
)
copy_button.pack(pady=10)

app.mainloop()