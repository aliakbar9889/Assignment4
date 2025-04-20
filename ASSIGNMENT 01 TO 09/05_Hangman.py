import random

def hangman():
    word_list = ["python", "hangman", "computer", "programming", "developer"]
    word = random.choice(word_list)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6  # Number of wrong guesses before hangman is fully drawn
    word_display = "_" * len(word)  # Display word with underscores for unguessed letters

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")

    while wrong_guesses < max_wrong_guesses:
        print("\nWord to guess: ", " ".join(word_display))
        print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")
        print("Guessed letters: ", ", ".join(guessed_letters))
        
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("❗ You already guessed that letter.")
        elif guess not in word:
            print(f"❌ Incorrect guess: {guess}")
            wrong_guesses += 1
            guessed_letters.append(guess)
        else:
            print(f"✅ Correct guess: {guess}")
            guessed_letters.append(guess)
            word_display = "".join([guess if word[i] == guess else word_display[i] for i in range(len(word))])

        if "_" not in word_display:
            print(f"\n🎉 Congratulations! You guessed the word: {word}")
            break

    if wrong_guesses == max_wrong_guesses:
        print(f"\n😞 Game Over! The word was: {word}")

# Run the game
hangman()
