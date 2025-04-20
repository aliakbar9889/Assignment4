# 04_tall_enough_to_ride

min_height: int = 50  # Correcting the variable declaration

def main():
    user = int(input('How tall are you? '))  # Correcting input conversion
    if user >= min_height:
        print('You are tall enough to ride')
    else:
        print('You are not tall enough to ride')

if __name__ == '__main__':
    main()