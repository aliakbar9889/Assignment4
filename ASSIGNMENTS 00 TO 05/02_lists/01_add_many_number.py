# 01_add_many_number

def add_many_number(*sum):
  result = 0
  for i in sum:
    result= result + i
  return result
result = add_many_number(25,56,23,58,96,12,25,65)
print(result)