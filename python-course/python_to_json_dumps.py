import json
person = {"Name": "Aqdas", "Age": 32}
person_json = json.dumps(person)
print (person_json)
print (type(person_json))