# 02_in_range.py

def in_range(n, low, high):
    """
    Yeh function check karta hai ki n low aur high ke beech hai ya nahi, inclusive.
    Agar n is range ke andar hai, to True return karega, warna False.
    """
    if n >= low and n <= high:
        return True
    return False

def main():
    # User se input lena
    n = int(input("Enter the number: "))
    low = int(input("Enter the low range: "))
    high = int(input("Enter the high range: "))
    
    # Result print karna
    print(in_range(n, low, high))  # in_range() ko call karke result print karna

if __name__ == '__main__':
    main()
