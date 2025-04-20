# 07_tiny_mad_lib

print("TINY MAD LIBS")

def main():
  noun: str = input('Enter a Noun: ')
  verb: str = input('Enter a verb: ')
  adj : str = input('Enter an adjective:' )
  print(f'Do you {verb} {adj} in {noun}?')

if __name__ == '__main__':
    main()