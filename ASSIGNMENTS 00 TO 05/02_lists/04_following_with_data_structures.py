# 04_flowing_with_data_structures

def copies(lst, data):
  for i in range(3):
      lst.append(data)
def message():
  message = input("Enter Your Message to copy : ")
  lst =[]
  print("List before:",lst)
  copies(lst, message)
  print("List after:",lst)

if __name__ == "__main__":
    message()
