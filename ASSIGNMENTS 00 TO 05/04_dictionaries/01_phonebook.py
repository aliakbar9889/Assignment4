# 01_phonebook


def read_phonebook():
    phonebook = {}  # Empty dictionary

    while True:
        name = input("Enter name (or press Enter to stop): ")
        if name == "":
            break

        number = input("Enter number: ")
        phonebook[name] = number  # Add name and number to phonebook

    return phonebook


def print_phonebook(phonebook):
    print("\nPhonebook:")
    for name in phonebook:
        print(name + " -> " + phonebook[name])

def search_phonebook(phonebook):
    while True:
        name = input("\nEnter name to search (or press Enter to stop): ")
        if name == "":
            break

        if name in phonebook:
            print(name + "'s number is: " + phonebook[name])
        else:
            print(name + " is not in the phonebook.")

# Main function to run the program
def main():
    phonebook = read_phonebook()     # Step 1: Input names and numbers
    print_phonebook(phonebook)       # Step 2: Print all entries
    search_phonebook(phonebook)      # Step 3: Search by name

# Call the main function
if __name__ == '__main__':
    main()
