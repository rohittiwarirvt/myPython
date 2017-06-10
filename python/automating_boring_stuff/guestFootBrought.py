guestAll = {
              'Rohit':{'apple': 2,'mango':4},
              'Rushabh' : {'banana':12, 'watermelon':2},
              'Rahul': {'grapes': 2,'cherry':29}

            }

def totalBrought(guests, item):
  numberOfItems = 0;
  for k,v in guests.items():
    numberOfItems = numberOfItems + v.get(item,0)
  return numberOfItems

print("Total Number of items with guys")
print("Apples -" + str(totalBrought(guestAll,'apple')))
print("Mango -" + str(totalBrought(guestAll,'mango')))
print("Banana -" + str(totalBrought(guestAll,'banana')))
print("Watermelon -" + str(totalBrought(guestAll,'watermelon')))
print("Grapes -" + str(totalBrought(guestAll,'grapes')))
print("Cherry -" + str(totalBrought(guestAll,'cherry')))
