import random
import string
from datetime import datetime

def generate_random_password(length=20):
    """Generate a random password with letters, digits, and special characters"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_passwords_to_file(num_passwords=10, filename="passwords.txt"):
    """Generate and save random passwords to a text file"""
    try:
        with open(filename, 'w') as file:
            file.write(f"Passwords generated on {datetime.now()}\n")
            file.write("=" * 50 + "\n\n")
            
            for i in range(num_passwords):
                password = generate_random_password()
                file.write(f"Password {i+1}: {password}\n")
        
        print(f"✓ {num_passwords} passwords saved to {filename}")
    except Exception as e:
        print(f"Error saving passwords: {e}")

if __name__ == "__main__":
    # Generate 10 passwords and save to file
    save_passwords_to_file(num_passwords=10, filename="passwords.txt")
