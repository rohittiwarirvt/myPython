import random

def printNumber(number):
  if number ==1:
    print('You have rock' + str(number))
  elif number ==2:
    print('You have pattice' + str(number))
  elif number == 3:
    print('You have shrewed' + str(number))
  elif number ==4:
    print('You have lolx' + str(number))
  elif number == 5:
    print('You have cadbury' + str(number))
  else:
    print("You r unique")
r = random.randint(1,6)
printNumber(r)
