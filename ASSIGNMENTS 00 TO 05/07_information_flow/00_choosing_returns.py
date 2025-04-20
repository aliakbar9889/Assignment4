# 00_choosing_returns.py

ADULT_AGE = 18  # U.S. age 

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    return False

def main():
    age = int(input("How old is this person?: "))  # User se age input lena
    print(is_adult(age))  # is_adult function ko call karna aur result print karna

if __name__ == "__main__":
    main()
