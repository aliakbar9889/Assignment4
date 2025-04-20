# 03_Wholesome_Machine

affirmation = "I am capable of doing anything I put my mind to."

def main():
    print('🌟 Welcome to the Wholesome Machine! 🌟')

    while True:
        user_input = input(f'💬 Please type the following affirmation exactly: \n👉 "{affirmation}"\n\nYour input: ')

        if user_input == affirmation:
            print('✅ That’s correct! You are amazing! 🎉💪')
            break
        else:
            print('❌ That’s incorrect. Try again! 😊')

if __name__ == '__main__':
    main()
