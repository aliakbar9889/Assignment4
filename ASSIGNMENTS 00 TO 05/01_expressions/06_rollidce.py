# 06_rolldice
import random
print("ROLL DICE")
def main():
  d1 : int = random.randint(1,6)
  d2 : int = random.randint(1,6)
  print(f'Total of Two Dice is : {d1+d2}')
if __name__ == '__main__':
    main()