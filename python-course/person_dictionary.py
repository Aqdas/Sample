person = {'name': "Aqdas", 'gender': 'Male', 'age': '32', 'address': 'Bahria Town Lahore', 'phone': '0333-7659229' }
key = input("What do you want to know about people?: ")
result = person.get(key, "invalid property") 
print (result)