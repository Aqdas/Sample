import requests
import json
import pprint
r = requests.get("https://opentdb.com/api.php?amount=1&category=21&difficulty=easy&type=multiple")
print(r.status_code)
print (r.text)
question = json.loads(r.text)
print (question)
pprint.pprint(question)
print (question ['results'][0]['category'])
print (question ['results'][0]["incorrect_answers"])