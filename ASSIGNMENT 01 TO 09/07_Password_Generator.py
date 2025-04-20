import random

def generate_password(length=8):
    # Characters to choose from
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    
    # Initialize an empty password string
    password = ""

    # Randomly pick characters and add to the password
    for i in range(length):
        password += random.choice(characters)

    return password

# Main
print("Welcome to the Simple Password Generator!")
password_length = int(input("Enter the desired password length (e.g., 8): "))

generated_password = generate_password(password_length)
print(f"Your generated password is: {generated_password}")
