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
entity = str(typeString.replace('http://www.wikidata.org/entity/',''))
print(entity)
if not os.path.exists('G:/rankings/'+entity+'.json'):
    for file in os.listdir("G:/results/"):
        if file.startswith(entity+'.json'):
            try:
                with open('G:/results/'+file,'r') as f:
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
                    errorFile.write('KeyError: '+entity+'\n')
            except JSONDecodeError as err:
                with open('G:/rankings/errors/jsonDecodeError.txt','a') as errorFile:
                    errorFile.write('JSONDecodeError: '+entity+' '+str(err)+'\n')

    
    outString = {
        'normal': normalRankCount,
        'preferred': preferredRankCount,
        'deprecated':deprecatedRankCount,
        'count':claimsTotalNumber
    }
    json_string = json.dumps(outString)
    with open('G:/rankings/'+entity+'.json','w') as output:
        output.write(json_string)
else:
    print('Skipped '+entity)
print('Total Statements: '+totalStatements)