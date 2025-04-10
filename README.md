# 💣 bobPassGen – Secure Password Generator

**bobPassGen** is a lightweight Python-based GUI tool designed to help users generate strong, secure, and customizable passwords with ease.  
It was developed as part of an internship project under the brand **BobXploit** 💻🛡️

---

## 🚀 Features

- ✅ Simple and intuitive GUI (built with Tkinter)
- 🎨 Dark-themed interface (black background with white/gray fonts)
- 🔐 Password includes:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- 🔧 User-defined password length
- 📋 Copy password to clipboard with one click
- 🖼️ Brand logo section included
- 👥 "About Us" section with clickable social media links
- 🧠 Lightweight and fast

---

## 🧰 Technologies Used

- **Python 3**
- `Tkinter` – GUI
- `random` – Password generation
- `pyperclip` – Copy to clipboard
- `webbrowser` – Open social media links
- `Pillow (PIL)` – Displaying the logo

---

## 🖼️ GUI Overview

- Logo placed at the top for branding
- Length input and checkboxes for password settings
- "Generate" button to create a password
- Display field for the generated password
- "Copy" button to quickly copy password
- About section + social media icons with working links

---

## 🏁 How to Run

```bash
git clone https://github.com/abanop22333/Secure-Password-Generator
sudo apt-get install python3-tk
cd bobPassGen
pip install -r requirements.txt
python bobPassGen.py
