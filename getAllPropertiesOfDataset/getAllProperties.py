import json
from operator import contains
import requests
from json.decoder import JSONDecodeError
import time
import os
properties = {}
counter = 0;
for file in os.listdir("G:/MusicalBand/data"):
    try:     
        with open('G:/MusicalBand/data/'+file,'r') as f:
            counter +=1;
            print(counter)
            data = json.load(f)       
            entities = data['entities']
            for key in entities: #entità Q
                el = entities[key]
                for claimsId in el['claims']: #proprietà P
                    statements = el['claims'][claimsId]
                    for elem in statements:
                        mainsnak = elem['mainsnak']
                        if(claimsId not in properties.keys()): 
                            toChange = {claimsId: 0} 
                            properties.update(toChange)
    except KeyError:
        print('key error')
        #with open('G:/asserted3/errors/rankingsError.txt','a') as errorFile:
            #errorFile.write(file)
    except JSONDecodeError as err:
        print('json error')
        
print(properties) 
with open('./allPropertiesMusical.json','w') as outfile:
    outfile.write(json.dumps(properties, indent = 4))