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

directory = 'G:\Dataset2\dataFromAPI'

for file in os.listdir(directory):
        try:
            print(file)
            path = os.path.join(directory, file)
            with open(path,'r') as f:
                data = json.load(f)               
                if 'entities' in data:
                    entities = data['entities']
                    for key in entities:
                        el = entities[key]
                        if 'claims' in el:
                            for claimsId in el['claims']:
                                statement = el['claims'][claimsId]
                                for elem in statement:
                                    claimsTotalNumber +=1
                                    totalStatements += 1
                                    if elem['rank'] == 'normal':
                                        normalRankCount +=1
                                    if elem['rank'] == 'preferred':
                                        preferredRankCount +=1        
                                    if elem['rank'] == 'deprecated':
                                        deprecatedRankCount +=1 
        except KeyError as err:
            print(err)
        except JSONDecodeError as err:
            print(err)


        
outString = {
    'normal': normalRankCount,
    'preferred': preferredRankCount,
    'deprecated':deprecatedRankCount,
    'count':claimsTotalNumber
}
json_string = json.dumps(outString)
with open('./countRankingDataset2.json','w') as output:
    output.write(json_string)
   