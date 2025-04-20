# 06_print_divisor.py

def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # Loop from 1 to num
        if num % i == 0:  # If i divides num without a remainder
            print(i)

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

if __name__ == '__main__':
    main()
