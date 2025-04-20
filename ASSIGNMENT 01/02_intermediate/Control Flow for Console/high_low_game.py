import random

NUM_ROUNDS = 5

def main():
    print("🎉 Welcome to the High-Low Game! 🎲")
    print("--------------------------------")

    score = 0

    for round_number in range(1, NUM_ROUNDS + 1):
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"\n🔢 Round {round_number}")
        print(f"🧍 Your number is {user_number}")
        guess = input("🤔 Do you think your number is 🔼 higher or 🔽 lower than the computer's?: ").lower()

        if guess == "higher":
            if user_number > computer_number:
                print(f"✅ You were right! 🎯 The computer's number was 💻 {computer_number}")
                score += 1
            elif user_number == computer_number:
                print(f"❌ It's a tie! But you don't get a point. The computer's number was 💻 {computer_number}")
            else:
                print(f"❌ Oops! You were wrong. The computer's number was 💻 {computer_number}")
        elif guess == "lower":
            if user_number < computer_number:
                print(f"✅ You were right! 🎯 The computer's number was 💻 {computer_number}")
                score += 1
            elif user_number == computer_number:
                print(f"❌ It's a tie! But you don't get a point. The computer's number was 💻 {computer_number}")
            else:
                print(f"❌ Oops! You were wrong. The computer's number was 💻 {computer_number}")
        else:
            print("⚠️ Please enter only 'higher' 🔼 or 'lower' 🔽.")
            continue

        print(f"🏅 Your score is now: {score}")

    print("\n🎮 Thanks for playing!")
    print(f"📊 Your final score is: {score}")

    if score == NUM_ROUNDS:
        print("🌟 Wow! You played perfectly! 🏆")
    elif score >= NUM_ROUNDS // 2:
        print("👍 Good job, you played really well! 💪")
    else:
        print("😅 Better luck next time! Keep practicing! 💡")

if __name__ == '__main__':
    main()
