# 01_Fibonacci Sequence

max_value = 10000

def main():
  a,b = 0,1
  print("✨Fibonacci Series : " , a, b ,end=' ')

  while True:
    c = a + b
    if c >= max_value:
     break
    print(c, end=' ')
    a,b = b,c

print("🎬 Sequence Complete")

if __name__ == '__main__':
  main()

