import tkinter as tk
from constants import *
from password_generator import generate_password


def copy_to_clipboard(password_field):
    """
    Copy the text content of a tkinter Entry widget to the system clipboard.

    Args:
        password_field: A tkinter Entry widget containing the text to be copied

    Returns:
        None
    """
    root = tk.Tk()
    # Hide the root
    root.withdraw()
    # Clear the clipboard
    root.clipboard_clear()
    # Copy the password to clipboard
    root.clipboard_append(password_field.get())
    # Update the root to reflect the clipboard change
    root.update()
    print(f"Password copied to clipboard: {password_field.get()}")
    # Close the root
    root.destroy()    

def generate_and_display_password(char_num, selected_types, password_field):
    """
    Generate a password and display it in a tkinter Entry widget.

    Args:
        char_num (int): The number of characters for the password
        selected_types (list): List of selected character types (e.g., 'Lowercase', 'Uppercase')
        password_field (tk.Entry): The tkinter Entry widget to display the password

    Returns:
        None
    """
    password = generate_password(char_num, selected_types)
    password_field.configure(state='normal')
    
    if password:
        password_field.delete(0, tk.END)
        password_field.insert(0, password)
        password_field.configure(state='readonly')
    else:
        password_field.delete(0, tk.END)
        password_field.insert(0, "Select at least one character type")
        password_field.configure(state='disabled')
    
    return password


