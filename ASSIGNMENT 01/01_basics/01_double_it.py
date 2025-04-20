# 01_double_it

def main():
    # User se input lein
    user_input = int(input("Enter a number: "))

    # Pehle use waise ka waise rakho
    curr_value = user_input

    # Loop chalayen jab tak curr_value 100 se chhoti ho
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")

    # Agar pehli value hi 100 ya zyada ho toh bhi show karein
    if curr_value == user_input:
        print(curr_value)

# Call the main function
if __name__ == '__main__':
    main()
