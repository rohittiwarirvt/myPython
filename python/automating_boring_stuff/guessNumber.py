import random

def main():
  print("Lets play number guessiong game")
  ans = random.randint(1,20)
  for i in range(1,7):
    print("Please take a guess")
    user_input = int(input())
    print("Ans is =>" + str(ans))
    if user_input < ans:
      print("The number seems to less")
    elif user_input > ans:
      print("The number is higher than the guess")
    else:
      break

  print("Ith coung" + str(i))

  if i < 6:
    print("Bro you guess the number correctly in " + str(i) + "Guesses")
  else:
    print("Bye Bye you were not able to guess number i am so sorry")

main()
