# 00_Guess_My_Number

print("❓ Guess My Number 🤔")

import random

def guess():
  secret_number = random.randint(1,100)
  guess = None
  while guess != secret_number:
    guess = int(input("🔍 Enter a Guess: "))

    if guess < secret_number:
       print('📉 Your guess is too low! Try again. ⬇️')

    elif guess > secret_number:
         print('📈 Your guess is too high! Try again. ⬆️')

    else:
          print(f'🏆 You guessed the correct number! 🧠💡 : {secret_number}')

if __name__ == '__main__':
  guess()
