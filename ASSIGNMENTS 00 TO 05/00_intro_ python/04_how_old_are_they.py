# 04_how_old_are_they

print("How Old Are They?")

def old():
    anton : int = 21
    beth : int = 6 + anton
    chen : int = 20 + beth
    drew  : int= chen + anton
    ethan : int = chen

    print(f'Anthon is {anton} year old')
    print(f'Beth is {beth} year old')
    print(f'Chen is {chen} year old')
    print(f'Drew is {drew} year old')
    print(f'Ethan is {ethan} year old')


if __name__ == "__main__":
  old()
