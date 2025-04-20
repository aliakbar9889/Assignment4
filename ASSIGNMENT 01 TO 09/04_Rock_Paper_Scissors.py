import random

def rock_paper_scissors():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    print("🎮 Let's play Rock, Paper, Scissors!")
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in options:
        print("❗ Invalid choice. Please choose rock, paper, or scissors only.")
        return

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("😐 It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")

# Run the game
rock_paper_scissors()
