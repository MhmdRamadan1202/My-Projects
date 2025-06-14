# import random as rd 
# import string 
# import tkinter as tk
# from tkinter import ttk, messagebox
# import pyperclip  # For copy to clipboard functionality

# lowercase=string.ascii_lowercase
# uppercase=string.ascii_uppercase
# digits=string.digits
# symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'

# def generate_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
#     characters=''
    
#     if use_lower:
#         characters+=lowercase
#     if use_upper:
#         characters+=uppercase
#     if use_digits:
#         characters+=digits
#     if use_symbols:
#         characters+=symbols
    
#     if not characters:
#         return "Error: At least one character type must be selected"
    
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password


# def get_user_input():
#     try:
#         length=int(input("Enter Password Lenth (defualt 12): " or 12))
#         lower=input("Include LowerCase letters? (y/n): ".lower()) !='n'
#         upper=input("Include UpperCase letters? (y/n): ".lower()) !='n'
#         digits = input("Include digits? (y/n): ").lower() != 'n'
#         symbols = input("Include symbols? (y/n): ").lower() != 'n' 
#         return length, lower, upper, digits, symbols
#     except ValueError:
#         print("Invalid input. Using default values.")
#         return 12, True, True, True, True

# def main():
#     print("=== Password Generator===")
#     length, lower, upper, digits, symbols=get_user_input()
#     password=generate_password(length, lower, upper, digits, symbols)
    
# if __name__=="__main__":
#     main()    
import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        
        self.create_widgets()  # This will now work because create_widgets is properly indented
    
    def create_widgets(self):
        # Title Label
        title_label = ttk.Label(self.root, text="Password Generator", font=('Helvetica', 16, 'bold'))
        title_label.pack(pady=10)
        
        # Length Frame
        length_frame = ttk.LabelFrame(self.root, text="Password Length")
        length_frame.pack(pady=10, padx=20, fill="x")
        
        self.length_var = tk.IntVar(value=12)
        length_slider = ttk.Scale(length_frame, from_=8, to=32, variable=self.length_var, 
                                command=lambda v: self.length_display.config(text=str(int(float(v)))))
        length_slider.pack(pady=5, padx=10, fill="x")
        
        self.length_display = ttk.Label(length_frame, text="12")
        self.length_display.pack()
        
        # Character Types Frame
        chars_frame = ttk.LabelFrame(self.root, text="Character Types")
        chars_frame.pack(pady=10, padx=20, fill="x")
        
        self.lower_var = tk.BooleanVar(value=True)
        lower_check = ttk.Checkbutton(chars_frame, text="Lowercase (a-z)", variable=self.lower_var)
        lower_check.pack(anchor="w", padx=10, pady=5)
        
        self.upper_var = tk.BooleanVar(value=True)
        upper_check = ttk.Checkbutton(chars_frame, text="Uppercase (A-Z)", variable=self.upper_var)
        upper_check.pack(anchor="w", padx=10, pady=5)
        
        self.digits_var = tk.BooleanVar(value=True)
        digits_check = ttk.Checkbutton(chars_frame, text="Digits (0-9)", variable=self.digits_var)
        digits_check.pack(anchor="w", padx=10, pady=5)
        
        self.symbols_var = tk.BooleanVar(value=True)
        symbols_check = ttk.Checkbutton(chars_frame, text="Symbols (!@#...)", variable=self.symbols_var)
        symbols_check.pack(anchor="w", padx=10, pady=5)
        
        # Generate Button
        generate_btn = ttk.Button(self.root, text="Generate Password", command=self.generate_password)
        generate_btn.pack(pady=20)
        
        # Password Display
        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(self.root, textvariable=self.password_var, font=('Courier', 12), 
                                  state='readonly', justify='center')
        password_entry.pack(pady=10, padx=20, fill="x")
        
        # Copy Button
        copy_btn = ttk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_btn.pack(pady=5)
    
    def generate_password(self):
        lowercase = string.ascii_lowercase if self.lower_var.get() else ''
        uppercase = string.ascii_uppercase if self.upper_var.get() else ''
        digits = string.digits if self.digits_var.get() else ''
        symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?' if self.symbols_var.get() else ''
        
        characters = lowercase + uppercase + digits + symbols
        
        if not characters:
            messagebox.showerror("Error", "Please select at least one character type")
            return
        
        password = ''.join(random.choice(characters) for _ in range(self.length_var.get()))
        self.password_var.set(password)
    
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password generated yet")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()