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

f = open('G:/tipi.json')
data = json.loads(f.read())    
noResponseCounter = 0
def isAnotherNormal(this,list):
    for elem in list:
        if(elem['rank'] == 'normal'):
                return True

def isAnotherDeprecated(this,list):
    for elem in list:
        if(elem['rank'] == 'deprecated'):
                return True

def isAnotherPreferred(this,list):
    for elem in list:
        if(elem['rank'] == 'preferred'):
                return True


for elem in data:
    notAssertedCount = 0
    assertedCount = 0
    claimsTotalNumber = 0
    typeString=elem['type']
    entity = str(typeString.replace('http://www.wikidata.org/entity/',''))
    print(entity) 
    if not os.path.exists('G:/asserted/'+entity+'.json'):
        for file in os.listdir("G:/results/"):
            claimsTotalNumber = 0
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
                                        if (isAnotherNormal(elem, statement)):
                                            assertedCount+=1
                                        elif (isAnotherPreferred(elem, statement)):
                                            notAssertedCount+=1     
                                        elif (isAnotherDeprecated(elem, statement)):
                                            assertedCount+=1
                                    if elem['rank'] == 'preferred':
                                        if(isAnotherPreferred(elem, statement)):
                                            assertedCount+=1     
                                        elif(isAnotherNormal(elem, statement)):
                                            assertedCount+=1
                                        elif(isAnotherDeprecated(elem, statement)):
                                            assertedCount+=1
                                    if elem['rank'] == 'deprecated':
                                        if(isAnotherDeprecated(elem, statement)):
                                            notAssertedCount+=1
                                        elif(isAnotherNormal(elem, statement)):
                                            notAssertedCount+=1
                                        elif(isAnotherPreferred(elem, statement)):
                                            notAssertedCount+=1     
                                       
                except KeyError:
                    with open('G:/rankings/errors/rankingsError.txt','a') as errorFile:
                        errorFile.write('KeyError: '+entity+'\n')
                except JSONDecodeError as err:
                    with open('G:/rankings/errors/jsonDecodeError.txt','a') as errorFile:
                        errorFile.write('JSONDecodeError: '+entity+' '+str(err)+'\n')

        
        outString = {
            'asserted': assertedCount,
            'notAsserted': notAssertedCount,
            'count':claimsTotalNumber
        }
        json_string = json.dumps(outString)
        with open('G:/asserted/'+entity+'.json','w') as output:
            output.write(json_string)
    else:
        print('Skipped '+entity)
print('Total Statements: '+str(totalStatements))