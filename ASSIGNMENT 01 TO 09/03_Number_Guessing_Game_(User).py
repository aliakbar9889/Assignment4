# 02_Number_Guessing_Game_(User).py


import random

def user_guess_number():
    secret_number = random.randint(1, 10)
    guess = None
    attempts = 0

    print("🎮 Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 10.\n")

    while guess != secret_number:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.\n")
            elif guess > secret_number:
                print("Too high! Try again.\n")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.\n")
        except ValueError:
            print("❗ Please enter a valid number.\n")

# Run the game
user_guess_number()
