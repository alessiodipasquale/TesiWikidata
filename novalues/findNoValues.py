from html import entities
import json
import os
from json.decoder import JSONDecodeError

counter = 0
for file in os.listdir("G:/Dataset3/results/results"):
    try:     
        with open('G:/Dataset3/results/results/'+file,'r') as f:
            data = json.load(f)       
            entities = data['entities']
            for key in entities: #entità Q
                el = entities[key]
                for claimsId in el['claims']: #proprietà P
                    statements = el['claims'][claimsId]
                    for elem in statements:
                        mainsnak = elem['mainsnak']
                        if(mainsnak['snaktype']=='novalue'):  
                            counter +=1
    except KeyError:
        print('key error')
        #with open('G:/asserted3/errors/rankingsError.txt','a') as errorFile:
            #errorFile.write(file)
    except JSONDecodeError as err:
        print('json error')
        
print(counter) 
    