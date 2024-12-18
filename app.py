import tkinter as tk
from tkinter import ttk
from utils import generate_and_display_password, copy_to_clipboard
from constants import CHECKBOXES



def main_frame():
    """
    Creates and displays the main application window with password generation controls.

    The window contains:
    - A slider for selecting password length
    - Checkboxes for character type options
    - An entry field to display the generated password
    - Buttons for generating password and copying to clipboard
    """
    
    # Create main window and set basic properties
    root = tk.Tk()
    root.iconbitmap('icon/password_generator.ico')
    root.title("Password Generator")
    root.geometry("400x500")
    style = ttk.Style()
    style.configure("TFrame", background='#f0f0f0')
    style.configure("TLabel", background='#f0f0f0',
                   font=('Helvetica', 12, 'bold'))
    style.configure("TCheckbutton", background='#f0f0f0',
                   font=('Helvetica', 10))
    style.configure("TButton", font=('Helvetica', 10, 'bold'),
                   padding=(20, 10))
    style.configure("Horizontal.TScale", background='#f0f0f0')
    style.configure("Authors.TLabel", background='#f0f0f0',
                   font=('Helvetica', 8), foreground='#666666')

    # Create main container with padding
    main_container = ttk.Frame(root, padding=(20, 20), style="TFrame")
    main_container.pack(expand=True, fill='both')

    # Create a label and slider for the password length
    password_len_lbl = ttk.Label(
        main_container,
        text="Password Length: 12",
        style="TLabel"
    )
    password_len_lbl.pack(pady=(0, 5))

    # Slider to select password length between 8 and 16 characters
    def update_length_label(value):
        """Update the password length label based on slider value."""
        password_len_lbl.config(text=f"Password Length: {int(float(value))}")

    password_len_sld = ttk.Scale(
        main_container,
        from_=8,
        to=16,
        orient=tk.HORIZONTAL,
        length=200,
        command=update_length_label
    )
    password_len_sld.set(12)  # Default value
    password_len_sld.pack(pady=(0, 20))

    # Create frame for checkboxes
    checkbox_frame = ttk.Frame(main_container, style="TFrame")
    checkbox_frame.pack(pady=(0, 20))

    # Create checkboxes for different character type options
    checkbox_vars = []
    
    # Create "Select All" checkbox
    select_all_var = tk.BooleanVar()

    def toggle_all():
        """Toggle all checkboxes based on the 'Select All' checkbox state."""
        state = select_all_var.get()
        for var in checkbox_vars:
            var.set(state)
    
    def update_select_all(*args):
        """Update 'Select All' checkbox based on individual checkboxes."""
        select_all_var.set(all(var.get() for var in checkbox_vars))

    select_all_checkbox = ttk.Checkbutton(
        checkbox_frame,
        text="Select All",
        variable=select_all_var,
        command=toggle_all,
        style="TCheckbutton"
    )
    select_all_checkbox.pack(pady=2, anchor='w')

    # Modified checkbox creation loop
    for text in CHECKBOXES:
        var = tk.BooleanVar()
        checkbox = ttk.Checkbutton(
            checkbox_frame,
            text=text,
            variable=var,
            command=update_select_all,  # Add this callback
            style="TCheckbutton"
        )
        var.set(True)
        checkbox.pack(pady=2, anchor='w')
        checkbox_vars.append(var)

    # Create a read-only entry field to display the generated password
    password_entry = ttk.Entry(
        main_container,
        state='readonly',
        width=30,
        font=('Helvetica', 12)
    )
    password_entry.configure(state='normal')
    password_entry.insert(0, "Generated password will appear here")
    password_entry.configure(state='disabled')
    password_entry.pack(pady=(0, 20))

    # Create button frame
    button_frame = ttk.Frame(main_container, style="TFrame")
    button_frame.pack(pady=(0, 30))

    def generate_password():
        """
        Generate a password based on the selected options and display it.
        """
        generate_and_display_password(
            int(password_len_sld.get()),
            [CHECKBOXES[i] for i in range(len(checkbox_vars))
             if checkbox_vars[i].get()],
            password_entry
        )
        if password_entry.get() not in [
            "",
            "Select at least one character type",
            "Generated password will appear here"
        ]:
            generate_btn.config(text="Password Generated")
            generate_btn.after(3000, lambda: generate_btn.config(
                text="Generate Password"))

    # Create button to generate password based on selected options
    generate_btn = ttk.Button(
        button_frame,
        text="Generate Password",
        command=generate_password,
        style="TButton"
    )
    generate_btn.pack(side=tk.LEFT, padx=5)

    def copy_password():
        """
        Copy the generated password to the clipboard if it is valid.
        """
        if (password_entry.get() and password_entry.get() not in [
            "",
            "Select at least one character type",
            "Generated password will appear here"
        ]):
            copy_to_clipboard(password_entry)
            copy_to_clipboard_btn.config(text="Password Copied!")
            copy_to_clipboard_btn.after(
                3000,
                lambda: copy_to_clipboard_btn.config(text="Copy to Clipboard")
            )

    # Create button to copy generated password to clipboard
    copy_to_clipboard_btn = ttk.Button(
        button_frame,
        text="Copy to Clipboard",
        command=copy_password,
        style="TButton"
    )
    copy_to_clipboard_btn.pack(side=tk.LEFT, padx=5)

    # Create authors label small size
    authors_label = ttk.Label(
        main_container,
        text="MaiorMajor 2024",
        style="Authors.TLabel"
    )
    authors_label.pack(side=tk.BOTTOM)

    # Start the main event loop
    root.mainloop()


if __name__ == "__main__":
    main_frame()