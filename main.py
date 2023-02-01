num = int(input('Type a number: '))

while num != 1:
  if num != 1:
    if num % 2 == 0:
      num = num / 2
      print(int(num))
    else:
      num += 1
      print(int(num))
  else:
    print(int(num))
  num = num