# 05_get_first_element

def get1stElement(lst):
  if lst:
    print(lst[0])
  else :
    print('List is Empty')

def getlist():
   lst=[]
   element = input("Enter an element and press enter to stop : ")
   while element != "":
      lst.append(element)
      element = input("Enter an element and press enter to stop: ")
   return lst

def main():
   lst = getlist()
   get1stElement(lst)



if __name__ == '__main__':
  main()
