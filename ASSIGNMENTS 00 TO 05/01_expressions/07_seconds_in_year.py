# 06_seconds_in_year

print("Seconds in a Year")

def main():
  seconds_in_minute : int = 60
  seconds_in_hour : int = 60 * 60
  seconds_in_day : int = 60 * 60 * 24
  seconds_in_year: int = seconds_in_day * 365
  print(f'There are {seconds_in_year} in a year.')

if __name__ == '__main__':
    main()