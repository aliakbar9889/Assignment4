# 07_get_list

def main():
  lst = []
  value =  input("Enter a value to add in the list ( press enter to stop ): ")

  while value:
    lst.append(value)
    value =  input("Enter a value to add in the list ( press enter to stop ): ")

  if lst:
    print("Here's Your final List", lst)

  else:
    print("Value did not exist")

if __name__ == '__main__':
  main()


