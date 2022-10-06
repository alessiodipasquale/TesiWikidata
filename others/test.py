from json.decoder import JSONDecodeError
import json
import os.path
import requests

f = open('random.json')
data = json.loads(f.read())    
noResponseCounter = 0
#7975
for elem in data:
    print(elem['type'])
#for typeString in range(0,7975):
 # typeString = data[i]['type']
  #entity = str(typeString.replace('http://www.wikidata.org/entity/',''))
  #print(entity)
  #filePath = 'G:/dumpSubject/' + entity+'.json'

 