blog_posts = ["","The 10 coolest math functions in Python", "How to make HTTP requests in Python","", "A tutorial about data types"]
for post in blog_posts:
  if post == "":
    continue
  else:
    print(post)
print ("---------------------------------")
myString = "This is a string"
for char in myString:
  print(char)
print ("---------------------------------")
for x in range(0,10):
  print(x)
print ("---------------------------------")
person = {"Name": "Aqdas Rehman", "Age": 25, "Gender": "Male"}
for key in person:
  print(key, ":", person[key])
print ("---------------------------------")
blog_posts = {"Python": ["The 10 coolest math functions in Python", "How to make HTTP requests in Python","A tutorial about data types"], "Javascript": ["Name spaces in Javascript", "Functions in Javascript"]}
for category in blog_posts:
  print ("Posts about", category)
  for post in blog_posts[category]:
    print(post)