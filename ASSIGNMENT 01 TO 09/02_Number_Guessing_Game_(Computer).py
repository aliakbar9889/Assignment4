# 02_Number_Guessing_Game_(Computer).py

import random

def computer_guess(limit):
    start = 1
    end = limit
    user_feedback = ""

    while user_feedback != 'c':
        if start <= end:
            computer_guess = random.randint(start, end)
        else:
            break

        user_feedback = input(f"Is your number {computer_guess}? Enter 'H' (too high), 'L' (too low), or 'C' (correct): ").lower()

        if user_feedback == 'h':
            end = computer_guess - 1
        elif user_feedback == 'l':
            start = computer_guess + 1

    print(f"Awesome! The computer guessed your number: {computer_guess}")

computer_guess(10)