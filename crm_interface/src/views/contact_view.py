import tkinter as tk
from tkinter import ttk, messagebox
import requests
from utils.tkinter_utils import make_inputs

API_BASE = "http://127.0.0.1:8000"

def fetch_contacts():
    try:
        response = requests.get(f"{API_BASE}/contacts")
        response.raise_for_status()
        contacts = response.json()["data"]["contacts"]

        # Clear table
        for row in tree.get_children():
            tree.delete(row)

        # Insert rows
        for contact in contacts:
            tree.insert("", "end", values=(contact["name"], contact["email"], contact["phone_number"], contact["last_contacted"]))
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch contacts: {e}")

def add_contact():
    name = name_var.get().strip()
    email = email_var.get().strip()
    phone_number = phone_number_var.get().strip()

    if not name or not email or not phone_number:
        messagebox.showwarning("Validation", "Name and Email are required")
        return
    try:
        response = requests.post(
            f"{API_BASE}/contacts",
            json={"name": name, "email": email, "phoneNumber": phone_number}
        )
        response.raise_for_status()
        fetch_contacts()
        name_var.set("")
        email_var.set("")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add contact: {e}")

# --- Tkinter App Setup ---
root = tk.Tk()
root.title("Snoodle CRM")
root.geometry("1920x1080")

# Menu bar
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

# Notebook (tabs)
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# --- Contacts Tab ---
contacts_tab = ttk.Frame(notebook)
notebook.add(contacts_tab, text="Contacts")

# Form for adding contacts
form_frame = ttk.Frame(contacts_tab, padding=5)
form_frame.pack(fill="x")

name_var = tk.StringVar()
email_var = tk.StringVar()
phone_number_var = tk.StringVar()

text_variables = [
    {"text": "Name:", "textvariable": name_var},
    {"text": "Email:", "textvariable": email_var},
    {"text": "Phone Number:", "textvariable": phone_number_var}
]

make_inputs(form_frame, text_variables)
ttk.Button(form_frame, text="Add Contact", command=add_contact).grid(row=0, column=len(text_variables) * 2, padx=5, pady=5)

# Contact list (table)
columns = ("name", "email", "phone_number", "last_contacted")
tree = ttk.Treeview(contacts_tab, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col.capitalize())
    tree.column(col, width=150)
tree.pack(fill="both", expand=True, pady=10)

# Refresh button
ttk.Button(contacts_tab, text="Refresh Contacts", command=fetch_contacts).pack(pady=5)

# Load contacts initially
fetch_contacts()

# Run app
root.mainloop()
