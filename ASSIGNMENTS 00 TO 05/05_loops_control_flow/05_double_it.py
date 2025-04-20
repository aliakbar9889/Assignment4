# 05_double_it

def main():
    # User se input lein
    user_input = int(input("Enter a number: "))

    # Us input ko curr_value mein store karo
    curr_value = user_input * 2

    # Jab tak curr_value 100 se chhota hai, loop chalta rahe
    while curr_value < 100:
        print(curr_value, end=" ")
        curr_value = curr_value * 2

    # Jab loop se bahar nikle (yaani value 100 ya usse zyada ho gayi), us value ko bhi print karo
    print(curr_value)


# Call the main function
if __name__ == '__main__':
    main()
