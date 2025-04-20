# 01_dicesimulator

import random

print("DICESIMULATOR")

def roll():
    dice1: int = random.randint(1, 6)
    dice2: int = random.randint(1, 6)
    total: int = dice1 + dice2
    print(f'Two Dice is : {total}')
    return dice1, dice2

def main():
    dice1: int = 10
    print("die1 in main() starts as: " + str(dice1))
    die1,die2 = roll()
    print(f'Rolled Dice : {die1},{die2}')
    die1,die2 = roll()
    print(f'Rolled Dice : {die1},{die2}')
    die1,die2 = roll()
    print(f'Rolled Dice : {die1},{die2}')

    print("die1 in main() is: " + str(die1))

if __name__ == '__main__':
    main()