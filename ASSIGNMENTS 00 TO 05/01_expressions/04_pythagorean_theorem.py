# 04_pythagorean_theorem
import math
print("PYTHOGOREAN THEOREM")

def main():
  AB : float = float(input('Enter The length of Side AB:'))
  AC : float = float(input("Enter The length of Side AC:"))
  BC : float = math.sqrt(AB ** 2 + AC ** 2)
  print("SIDE AB = " + str(AB))
  print("SIDE AC = " + str(AC))
  print("SIDE BC (which required) = " + str(BC))

if __name__ == '__main__':
    main()

