from json.decoder import JSONDecodeError
import json
import os.path
import requests
import time

f = open('random.json')
data = json.loads(f.read())    
noResponseCounter = 0

for elem in data:
  typeString=elem['type']
  entity = str(typeString.replace('http://www.wikidata.org/entity/',''))
  print(entity)
  filePath = 'G:/dumpSubject/' + entity+'.json'
  if not os.path.exists(filePath):
    url = 'https://query.wikidata.org/sparql'
    query = """
    select ?s 
    {

    ?s wdt:P31 wd:%s
    }
    """ % entity
    try:
      r = requests.get(url, params = {'format': 'json', 'query': query})
      r.raise_for_status()
      data = r.json()
      resultCount = len(data['results']['bindings'])
      items = []
      for item in data['results']['bindings']:
        items.append(item)
      with open(filePath, 'w') as json_file:
         json.dump(items, json_file, 
                            indent=4,  
                            separators=(',',': '))
      print("Saved to JSON: %s" % entity)
      time.sleep(1)
    except requests.exceptions.HTTPError as errh:
        noResponseCounter += 1
        print(errh)
        #time.sleep(120)
    except requests.exceptions.ConnectionError as errc:
        noResponseCounter += 1
        print(errc)
        #time.sleep(120)
    except requests.exceptions.Timeout as errt:
        noResponseCounter += 1
        print(errt)
        #time.sleep(120)
    except requests.exceptions.RequestException as err:
        noResponseCounter += 1
        print(err)
        #time.sleep(120)
    except JSONDecodeError as err:
        noResponseCounter += 1
        print(err) 
    except NameError as err:
        noResponseCounter += 1
        print (err)
  

