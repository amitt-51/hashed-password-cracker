import tkinter as tk
from tkinter import messagebox
from cracker import crack_hash

class PasswordCrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hashed Password Cracker")
        self.root.geometry("500x500")
        
        self.wordlist_path = "wordlist.txt"  # Update this path

        
        tk.Label(root, text="Enter Hashed Password:").pack(pady=5)
        self.hash_entry = tk.Entry(root, width=60)
        self.hash_entry.pack()


        tk.Label(root, text="Select Hash Type:").pack(pady=5)
        self.hash_type_var = tk.StringVar(value="md5")  # Default value
        hash_types = ["md5", "sha1", "sha256", "sha512"]
        self.hash_type_menu = tk.OptionMenu(root, self.hash_type_var, *hash_types)
        self.hash_type_menu.pack(pady=5)

        tk.Button(root, text="Start Cracking", command=self.start_cracking).pack(pady=10)

        tk.Label(root, text="Output:").pack()
        self.output_text = tk.Text(root, height=18, width=60)
        self.output_text.pack(pady=5)

    def start_cracking(self):
        hash_value = self.hash_entry.get().strip()
        hash_type = self.hash_type_var.get()

        # Validate hash type
        if hash_type not in ["md5", "sha1", "sha256", "sha512"]:
            messagebox.showerror("Hash Type Error", "⚠️ Invalid hash type selected.")
            return

        if not hash_value:
            messagebox.showerror("Input Error", "Please enter a hash before starting.")
            return

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert("end", "Cracking started...\n")

        # Use the predefined wordlist for cracking
        crack_hash(hash_value, self.wordlist_path, self.output_text, hash_type)
