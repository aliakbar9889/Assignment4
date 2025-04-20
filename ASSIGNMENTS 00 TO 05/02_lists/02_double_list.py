# 02_double_list

def double():
  num:list[int] = [1,2,3,4]
  double_num = []
  for number in num:
    double_num.append(number * 2)
  return double_num

result = double()
print (result)

