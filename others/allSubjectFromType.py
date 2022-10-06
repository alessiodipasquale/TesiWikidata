
import json

f = open('random.json')
data = json.loads(f.read())    

print (data)

print(data[1]['type'])  
