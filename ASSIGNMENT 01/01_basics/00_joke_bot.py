# 00_joke_bot

JOKE = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs 😂😀'"
SORRY = "Sorry ! I can only tell jokes"

def main():

  print("WELCOME TO A.A J😂KE BOT")

  user_input = input("What do you want? ").strip().lower()
  if "joke" in user_input:
    print(JOKE)

  else:
    print(SORRY)

if __name__ == "__main__":
 main()
