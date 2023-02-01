while True:
  try:
    num = int(input('Type a number: '))
  except ValueError:
    print("That's not an integer number")
    num = int(input('Type a number: '))
  
    while num != 1:
      if num != 1:
        if num % 2 == 0:
          num = num / 2
          print(int(num))
        else:
          num = num * 3 + 1
          print(int(num))
      else:
        print(int(num))
      num = num
  break
  