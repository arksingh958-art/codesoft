import tkinter as tk
from tkinter import messagebox
import random
import string


# ---------------- PASSWORD GENERATOR ----------------

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning(
                "Invalid Length",
                "Password length should be at least 4."
            )
            return

        characters = ""

        if lowercase_var.get():
            characters += string.ascii_lowercase

        if uppercase_var.get():
            characters += string.ascii_uppercase

        if numbers_var.get():
            characters += string.digits

        if symbols_var.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showwarning(
                "No Character Type",
                "Please select at least one character type."
            )
            return

        password = ''.join(
            random.choice(characters)
            for _ in range(length)
        )

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid password length."
        )


# ---------------- COPY PASSWORD ----------------

def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            "No Password",
            "Generate a password first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard!"
    )


# ---------------- CLEAR ----------------

def clear_password():
    password_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    length_entry.insert(0, "12")

    lowercase_var.set(True)
    uppercase_var.set(True)
    numbers_var.set(True)
    symbols_var.set(True)


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()

root.title("Password Generator")
root.geometry("550x600")
root.resizable(False, False)


# ---------------- HEADER ----------------

header = tk.Label(
    root,
    text="🔐 PASSWORD GENERATOR",
    font=("Arial", 22, "bold")
)

header.pack(pady=25)


subtitle = tk.Label(
    root,
    text="Create a strong and secure random password",
    font=("Arial", 11)
)

subtitle.pack(pady=5)


# ---------------- MAIN FRAME ----------------

main_frame = tk.Frame(
    root,
    padx=30,
    pady=20
)

main_frame.pack(fill="both", expand=True)


# ---------------- PASSWORD LENGTH ----------------

tk.Label(
    main_frame,
    text="Password Length",
    font=("Arial", 12, "bold")
).pack(anchor="w", pady=(10, 5))


length_entry = tk.Entry(
    main_frame,
    font=("Arial", 13),
    width=20,
    justify="center"
)

length_entry.pack(pady=5)

length_entry.insert(0, "12")


# ---------------- CHARACTER OPTIONS ----------------

tk.Label(
    main_frame,
    text="Password Complexity",
    font=("Arial", 12, "bold")
).pack(anchor="w", pady=(20, 5))


lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)


tk.Checkbutton(
    main_frame,
    text="Lowercase Letters (a-z)",
    variable=lowercase_var,
    font=("Arial", 11)
).pack(anchor="w")


tk.Checkbutton(
    main_frame,
    text="Uppercase Letters (A-Z)",
    variable=uppercase_var,
    font=("Arial", 11)
).pack(anchor="w")


tk.Checkbutton(
    main_frame,
    text="Numbers (0-9)",
    variable=numbers_var,
    font=("Arial", 11)
).pack(anchor="w")


tk.Checkbutton(
    main_frame,
    text="Symbols (!@#$...)",
    variable=symbols_var,
    font=("Arial", 11)
).pack(anchor="w")


# ---------------- GENERATE BUTTON ----------------

generate_button = tk.Button(
    main_frame,
    text="⚡ Generate Password",
    font=("Arial", 12, "bold"),
    command=generate_password,
    padx=15,
    pady=8
)

generate_button.pack(pady=25)


# ---------------- PASSWORD DISPLAY ----------------

tk.Label(
    main_frame,
    text="Generated Password",
    font=("Arial", 12, "bold")
).pack(anchor="w", pady=5)


password_entry = tk.Entry(
    main_frame,
    font=("Arial", 14),
    width=40,
    justify="center"
)

password_entry.pack(pady=8)


# ---------------- BUTTONS ----------------

button_frame = tk.Frame(main_frame)
button_frame.pack(pady=15)


tk.Button(
    button_frame,
    text="📋 Copy",
    font=("Arial", 11, "bold"),
    command=copy_password,
    width=12
).grid(row=0, column=0, padx=5)


tk.Button(
    button_frame,
    text="🗑 Clear",
    font=("Arial", 11, "bold"),
    command=clear_password,
    width=12
).grid(row=0, column=1, padx=5)


# ---------------- FOOTER ----------------

footer = tk.Label(
    root,
    text="CodeSoft Python Project | Password Generator",
    font=("Arial", 9)
)

footer.pack(pady=10)


# ---------------- START APPLICATION ----------------

root.mainloop()