# 04_random_numbers

import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 99

def main():
    for _ in range(N_NUMBERS):
        value = random.randint(MIN_VALUE, MAX_VALUE)
        print(value, end=" ")

if __name__ == '__main__':
    main()
