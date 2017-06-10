def divideBy(number):
  try:
    return 12/number
  except ZeroDivisionError:
    print('Error: Invalid argument')

divideBy(2)
divideBy(4)
divideBy(3)
#divideBy(0)
