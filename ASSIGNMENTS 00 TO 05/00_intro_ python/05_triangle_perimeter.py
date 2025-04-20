# 05_triangle_perimeter
def perimeter():
  print("Calculation of Perimeter of Triangle")
  side1 : float = float(input('Enter Your First Side of Triangle'))
  side2 : float = float(input('Enter Your Second Side of Triangle'))
  side3 : float = float(input('Enter Your Third Side of Triangle'))
  peri : float = float(side1 + side2 + side3)

  print(f'The perimeter of triangle is {peri}')

if __name__ == '__main__':
    perimeter()
