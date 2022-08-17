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


normalRankCount = 0
preferredRankCount = 0
deprecatedRankCount = 0
claimsTotalNumber = 0
for file in os.listdir("/home/admin/musicalband/data"):
        try:
            with open('/home/admin/musicalband/data/'+file,'r') as f:
                data = json.load(f)               
                entities = data['entities']
                for key in entities:
                    el = entities[key]
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
        except KeyError:
            with open('G:/rankings/errors/rankingsError.txt','a') as errorFile:
                print("Error")
        except JSONDecodeError as err:
            with open('G:/rankings/errors/jsonDecodeError.txt','a') as errorFile:
                print("Error")


outString = {
    'normal': normalRankCount,
    'preferred': preferredRankCount,
    'deprecated':deprecatedRankCount,
    'count':claimsTotalNumber
}
json_string = json.dumps(outString)
with open('/home/admin/musicalband/ranking.json','w') as output:
    output.write(json_string)

print('Total Statements: '+str(totalStatements))