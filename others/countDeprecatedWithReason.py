from html import entities
import json
import os
from json.decoder import JSONDecodeError
directory = './'
normalRankCount = 0
preferredRankCount = 0
deprecatedRankCount = 0
claimsTotalNumber = 0
totalStatements = 0
noResponseCounter = 0
counter=0;

elements = {}

for file in os.listdir("G:/Dataset3/results/results"):
    preferredRankCount +=1
    print(preferredRankCount)
    try:
        with open('G:/Dataset3/results/results/'+file,'r') as f:
            data = json.load(f)               
            entities = data['entities']
            for key in entities:
                el = entities[key]
                for claimsId in el['claims']:
                    statement = el['claims'][claimsId]
                    for elem in statement:
                        claimsTotalNumber +=1
                        totalStatements += 1   
                        if elem['rank'] == 'deprecated' and ("P2241" in elem["qualifiers-order"]):
                            for qualifier in elem['qualifiers']:
                                if(qualifier == "P2241"):
                                    noval = elem['qualifiers'][qualifier]
                                    qualifier = noval[0]['datavalue']['value']['id']
                                    if(qualifier not in elements):
                                        toChange = {qualifier: 1} 
                                        elements.update(toChange)
                                    else:
                                        toChange = {qualifier: elements.get(qualifier)+1}
                                        elements.update(toChange) 
                            counter+=1 
    except KeyError:
        with open('G:/rankings/errors/rankingsError.txt','a') as errorFile:
            noResponseCounter+=1
    except JSONDecodeError as err:
        with open('G:/rankings/errors/jsonDecodeError.txt','a') as errorFile:
            noResponseCounter+=1
print('totale:'+ str(counter))

data = sorted(elements.items(), key = lambda item: item[1], reverse=True)

json_string = json.dumps(data)
with open('C:/Users/aless/Desktop/Tesi/dataset3/reasonOfDeprecation3.json','w') as output:
    output.write(json_string)
