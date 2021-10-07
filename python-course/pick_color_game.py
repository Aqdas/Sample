import random
colors = ["black","white","gray","yellow","purple","green","maroon","blue"]

while True:
  color = colors[random.randint(0,len(colors)-1)]
  guess_color = input("I'm thinking about a color, can you guess it? ")
  while True:
    if (color == guess_color.lower()):
      break
    else:
      guess_color = input("Nope. Try again: ")
  print("You guessed it Right! I was thinking about", color)
  play_again = input("Let's play again? Type 'no' to quit.")
  if play_again.lower() == 'no':
    break
print("it was fun, thanks for playing!")