import random
import string

def generate_password(char_num: int, checkboxes: list):
    """
    Generate a random password based on the specified character count and checkbox selections.

    Args:
        char_num (int): The number of characters in the password.
        checkboxes (list): A list of checkbox selections.

    Returns:
        str: The generated password or None if no character types are selected.
    """
    password = ""
    char_set = ""

    # Add character sets based on checkbox selections
    if "Lowercase" in checkboxes:
        char_set += string.ascii_lowercase
    if "Uppercase" in checkboxes:
        char_set += string.ascii_uppercase
    if "Numbers" in checkboxes:
        char_set += string.digits
    if "Symbols" in checkboxes:
        char_set += string.punctuation

    # If no checkboxes are selected, return None
    if not char_set:
        return None

    # Generate password by randomly selecting characters from the char_set
    for _ in range(char_num):
        password += random.choice(char_set)

    return password