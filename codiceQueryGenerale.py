from json.decoder import JSONDecodeError
import requests
import json
from datetime import datetime
import sys
import time
import os.path
numberOfMaxError = 2


file_exists = os.path.exists("drive/MyDrive/wikidata/dump/data-%s.json" % index)

limit = 10000
offset = 0
resultCount = limit
i = 1
#filePath = "dump/data-%s.json" % now
#jsonFile = open(filePath, "w")
timeSleep = 1
noResponseCounter = 0
while resultCount == limit:
  filePath = "dump/data-%s.json" % i
  if not os.path.exists(filePath):
    url = 'https://query.wikidata.org/sparql'
    query = """
    select ?s ?p ?o1 ?o2
    {

    ?s ?px ?statement1.
    ?statement1 ?p ?o1.

    ?statement1 wikibase:rank wikibase:DeprecatedRank.
    ?s ?py ?statement2.
    ?statement2 ?p ?o2.

    ?statement2 wikibase:rank wikibase:NormalRank.

    }
    limit %s
    offset %s
    """ % (limit, offset)
    try:
      r = requests.get(url, params = {'format': 'json', 'query': query})
      r.raise_for_status()
      print(r)
      data = r.json()
      resultCount = len(data['results']['bindings'])
      items = []
      for item in data['results']['bindings']:
        items.append(item)
      with open(filePath, 'w') as json_file:
        
        json.dump(items, json_file, 
                            indent=4,  
                            separators=(',',': '))
      print("Saved to JSON: %s" % i)
      time.sleep(timeSleep)
      print("Index:%s, offset:%s, resultCount:%s" % (i,offset, len(data['results']['bindings'])))

        # Code here will only run if the request is successful
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
  else:
    print("Skipped %s" % i)
  offset += limit
  i+=1
  if noResponseCounter == numberOfMaxError:
      os.system('clear')
      print("Resetting...")
      noResponseCounter = 0
      i = 1
      offset = 0
      time.sleep(120)
      
 
print('Successfully appended to the JSON file')

