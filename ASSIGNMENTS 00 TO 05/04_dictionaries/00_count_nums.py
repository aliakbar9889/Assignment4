# 00_count_num

def count_num():
    count_dict = {}

    while True:
        num = input('Enter a Number (or press Enter to quit): ')

        if num.lower() == "" :
            break

        if num.isdigit():
            num = int(num)
            count_dict[num] = count_dict.get(num, 0) + 1
            print(count_dict)
        else:
            print('Invalid Input!')

    return count_dict

def show(count_dict):
    print('\nNumber\t\tCount:')
    for num, count in count_dict.items():
        print(f'{num}\t\t{count}')

if __name__ == '__main__':
    count_dict = count_num()  # Store returned dictionary
    show(count_dict)  # Call show function