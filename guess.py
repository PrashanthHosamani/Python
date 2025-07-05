#guessing game

import random
jackpot = random.randint(1, 100)


guess = int(input("Guess the number: "))
counter = 1
while guess != jackpot:
  if guess < jackpot:
    print("wrong answer, guess heigher")
  else:
    print("wrong answer, guess lower")

  guess = int(input("Guess the number"))
  counter += 1
else:
  print("Correct answer")
  print("attempts", counter)


