# 02_international_voting_age

print('CALCULATE YOUR VOTING AGE')

PETURKSBOUIPO: int = 16
STANLAU: int = 25
MAYENGUA: int = 48

def main():
    age: int = int(input('How old are you? '))  # Input as integer

    if age >= PETURKSBOUIPO:
        print(f'Your age is {age}. You are eligible to vote in PETURKSBOUIPO.')
    else:
        print(f'Your age is {age}. You are not eligible to vote in PETURKSBOUIPO.')

    if age >= STANLAU:
        print(f'Your age is {age}. You are eligible to vote in STANLAU.')
    else:
        print(f'Your age is {age}. You are not eligible to vote in STANLAU.')

    if age >= MAYENGUA:
        print(f'Your age is {age}. You are eligible to vote in MAYENGUA.')
    else:
        print(f'Your age is {age}. You are not eligible to vote in MAYENGUA.')

if __name__ == '__main__':
    main()



