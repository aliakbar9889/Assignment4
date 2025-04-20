# 05_remainder_division
print("REMAINDER DIVISION")

def main():
  num1 : int = int(input('Enter your first number :'))
  num2 : int = int(input('Enter your second number :'))

  quotient : int = num1 // num2
  remainder : int = num1 % num2

  print(f'The Quotient is {quotient} & Remainder is {remainder} for {num1} divided by {num2}')

  if remainder == 0:
     print(f'{num1} is completely divisible by {num2}.')
  else:
     print(f'{num1} is not completely divisible by {num2}.')

if __name__ == '__main__':
    main()