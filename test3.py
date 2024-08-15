import random
import string

def generate_password(length=12):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None
    
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Ensure the password includes at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest of the password length with random choices from all sets
    all_characters = lower + upper + digits + special
    password += random.choices(all_characters, k=length-4)
    
    # Shuffle the resulting password list to ensure randomness
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)

# Get the desired password length from the user
length = int(input("Enter the desired password length (minimum 4): "))
password = generate_password(length)

if password:
    print(f"Generated password: {password}")