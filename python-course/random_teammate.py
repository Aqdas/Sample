import random
teammates = []
for name in range(0,8):
  names = input ("Type the name of your teammates: ")
  teammates.append(names)

index = random.randint(0,7)
random_teammate = teammates[index]
print("Picking a random teammate name: ", random_teammate)