# 03_fehrenheit_to_celsius

print("Fehrenheit To Celsius Converter")
def convert():
  fehrenheit = float(input('Enter Your Fehrenheit Value:'))
  celsius = (fehrenheit - 32) * 5.0/9.0
  print(f'Your Celsius Value of {fehrenheit} is {celsius}')

if __name__ == "__main__":
 convert()


