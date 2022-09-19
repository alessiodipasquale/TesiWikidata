from html import entities
import json
import os
from json.decoder import JSONDecodeError

f = open('G:/tipi.json')
data = json.loads(f.read()) 
for elem in data:
    counter = 0
    typeString=elem['type']
    entity = str(typeString.replace('http://www.wikidata.org/entity/',''))
    print(entity) 
    if not os.path.exists('G:/novalues1/'+entity+'.json'):
        for file in os.listdir("G:/results/"):
            if file.startswith(entity+'.json'):        
                try:     
                    with open('G:/results/'+file,'r') as f:
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
        outString = {
                'novalues': counter,
        }
        json_string = json.dumps(outString)
        with open('G:/novalues1/'+entity+'.json','w') as output:
            output.write(json_string)
    else:
        print('Skipped '+entity)    
print(counter) 
    