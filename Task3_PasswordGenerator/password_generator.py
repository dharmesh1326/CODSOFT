# Task 3: Password Generator
# Author: Dharmesh J
# Date: 05.06.25

import random
import string

def get_password_settings():
    length = int(input("Enter desired password length: "))
    include_letters = input("Include letters? (y/n): ").lower() == 'y'
    include_digits = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    return length, include_letters, include_digits, include_symbols
def generate_password(length, use_letters, use_digits, use_symbols):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character type must be selected.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Welcome to the Password Generator!")
    length, use_letters, use_digits, use_symbols = get_password_settings()
    password= generate_password(length, use_letters, use_digits, use_symbols)
    print(f"Generated Password: {password}")
if __name__ == "__main__":
    main()
# This code generates a random password based on user-defined settings.
# It allows the user to specify the length and types of characters to include.
