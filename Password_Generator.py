import random
import string

def generate_password(length=12, include_special=True):
    # Generates a password based on length and special character preference
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation if include_special else ''
    all_chars = letters + digits + specials
    if not all_chars:
        raise ValueError("No characters available to generate password.")
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def save_password_to_file(password, filename='password.txt'):
    # Appends the password to a text file
    try:
        with open(filename, 'a') as f:
            f.write(password + '\n')
        print(f"Password saved to {filename}")
    except IOError as e:
        print(f"Error saving password: {e}")

if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        special_input = input("Include special characters? (y/n): ").lower()
        include_special = special_input == 'y'
        password = generate_password(length, include_special)
        print("Generated Password:", password)
        save_password_to_file(password)
    except ValueError:
        print("Invalid input. Please enter a number for length.")

