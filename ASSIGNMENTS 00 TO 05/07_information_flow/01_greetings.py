# 01_greetings.py

def greet(name):
    return "Greetings " + name + "!"

def main():
    name = input("What's your name? ")  # Asking the user for their name
    print(greet(name))  # Calling the greet function and printing the greeting

if __name__ == '__main__':
    main()
