import random
counter = 0
number = random.randint(0,10)
guess = int (input("I'm thinking about a number between zero and ten. Can you guess it? "))

while True:

  if counter >= 2:
    print("You lost")
    break
  
  if guess == number:
    print ("You guessed it. I was thinking about", number)
    break
  else:
    guess = int (input ("Nope. Try again: "))
  
  counter +=1
