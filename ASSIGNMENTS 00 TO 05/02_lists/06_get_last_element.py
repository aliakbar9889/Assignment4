# 06_get_last_element

def get_Last_Element(lst):
  if lst:
    print(lst[-1])
  else :
    print('List is Empty')

def getlist():
   lst=[]
   element = input("Enter an element or ( press enter to stop ) : ")
   while element != "":
      lst.append(element)
      element = input("Enter an element or ( press enter to stop: ) ")
   return lst

def main():
   lst = getlist()
   get_Last_Element(lst)



if __name__ == '__main__':
  main()