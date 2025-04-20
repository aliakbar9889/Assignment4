# 08_shorten

Max_length = 3

def shorten(lst):
    while len(lst) > Max_length:  # Checking if list size is greater than max allowed length
        last_element = lst.pop()
        print("Removed:", last_element)  # Showing removed elements

    print("Final shortened list:", lst)  # Printing final list after shortening

def get_lst():
    lst = []
    element = input('Enter an element to add to the list: ')  # Fixed typo

    while element != "":  # Keep taking input until empty
        lst.append(element)
        element = input('Enter an element to add to the list: ')

    return lst

def main():
    lst = get_lst()  # Get user input list
    shorten(lst)  # Shorten the list if needed

if __name__ == '__main__':
    print('08_shorten')
    main()