# 02_e=mc2

print("Einstein Formula For Energy")

def energy():
  c: float = 299792458
  m: float = float((input('Enter Your Mass in kg :')))

  print('e = m * C^2')
  print('m = ' + str(m) + "kg")
  print('c = ' + str(c) + 'm/s')
  print("======================")
  print("e = " + str(m * c ** 2) + " Joules")

if __name__ == '__main__':
    energy()


