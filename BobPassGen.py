import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import string
import webbrowser
import pyperclip

def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")
        return

    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    if not (use_upper or use_lower or use_digits or use_special):
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)

def copy_password():
    pyperclip.copy(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def open_link(url):
    webbrowser.open(url)

# Main window
root = tk.Tk()
root.title("bobPassGen")
root.geometry("600x750")
root.config(bg="black")

# Styles
font_title = ("Arial", 16, "bold")
font_normal = ("Arial", 12)
fg_color = "white"
bg_color = "black"
button_color = "#1E1E1E"
entry_bg = "#2B2B2B"

# === Logo Section ===
logo_image = Image.open("logo-white.png")
logo_image = logo_image.resize((180, 180))
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo, bg=bg_color)
logo_label.pack(pady=10)

# === Password Settings ===
tk.Label(root, text="Select Password Length:", font=font_normal, bg=bg_color, fg=fg_color).pack()
length_var = tk.StringVar(value="12")
tk.Entry(root, textvariable=length_var, bg=entry_bg, fg=fg_color, font=font_normal, insertbackground="white").pack(pady=5)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var, bg=bg_color, fg=fg_color, font=font_normal, selectcolor=entry_bg, activebackground=bg_color, activeforeground=fg_color).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var, bg=bg_color, fg=fg_color, font=font_normal, selectcolor=entry_bg, activebackground=bg_color, activeforeground=fg_color).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Digits", variable=digits_var, bg=bg_color, fg=fg_color, font=font_normal, selectcolor=entry_bg, activebackground=bg_color, activeforeground=fg_color).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var, bg=bg_color, fg=fg_color, font=font_normal, selectcolor=entry_bg, activebackground=bg_color, activeforeground=fg_color).pack(anchor="w", padx=20)

# === Generate Button ===
tk.Button(root, text="Generate Password", command=generate_password, bg=button_color, fg="white", font=font_normal).pack(pady=10)

# === Password Output ===
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, width=40, font=font_normal, bg=entry_bg, fg=fg_color, insertbackground="white").pack()

# === Copy Button ===
tk.Button(root, text="Copy to Clipboard", command=copy_password, bg=button_color, fg="white", font=font_normal).pack(pady=5)

# === About Us ===
tk.Label(root, text="About Us", font=("Arial", 13, "bold"), bg=bg_color, fg=fg_color).pack(pady=10)
tk.Label(root, text="bobPassGen is a secure password generator tool by BobXploit.\nThink Like a Hacker, Protect Like a Pro.",
         wraplength=400, justify="center", bg=bg_color, fg=fg_color, font=font_normal).pack()

# === Social Links ===
tk.Label(root, text="Connect with us:", font=("Arial", 12, "bold"), bg=bg_color, fg=fg_color).pack(pady=10)

social_frame = tk.Frame(root, bg=bg_color)
social_frame.pack()

tk.Button(social_frame, text="github", command=lambda: open_link("https://github.com/abanop22333"),
          bg=button_color, fg="white", font=font_normal).grid(row=0, column=0, padx=5)
tk.Button(social_frame, text="Facebook", command=lambda: open_link("https://www.facebook.com/profile.php?id=100034421751715"),
          bg=button_color, fg="white", font=font_normal).grid(row=0, column=1, padx=5)
tk.Button(social_frame, text="X Platform", command=lambda: open_link("https://x.com/AbanoubE4130"),
          bg=button_color, fg="white", font=font_normal).grid(row=0, column=2, padx=5)
tk.Button(social_frame, text=" linkedin", command=lambda: open_link("https://instagram.com/yourprofile"),
          bg=button_color, fg="white", font=font_normal).grid(row=0, column=3, padx=5)

root.mainloop()
