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

#f = open('G:/tipi.json')
#data = json.loads(f.read())    
noResponseCounter = 0
def isAnotherNormal(this,list):
    for elem in list:
        if(elem['rank'] == 'normal'  and elem != this):
                return True

def isAnotherDeprecated(this,list):
    for elem in list:
        if(elem['rank'] == 'deprecated'  and elem != this):
                return True

def isAnotherPreferred(this,list):
    for elem in list:
        if(elem['rank'] == 'preferred' and elem != this):
                return True


#for elem in data:
notAssertedCount = 0
assertedCount = 0
claimsTotalNumber = 0
    #typeString=elem['type']
    #entity = str(typeString.replace('http://www.wikidata.org/entity/',''))
    #print(entity) 
    #if not os.path.exists('G:/asserted3/'+entity+'.json'):
for file in os.listdir("G:/Dataset2/dataFromAPI"):
    print(file)
    claimsTotalNumber = 0
    #if file.startswith(entity+'.json'):
    try:     
        with open('G:/Dataset2/dataFromAPI/'+file,'r') as f:
        #with open('C:/Users/aless/Desktop/Tesi/asserted/input/input.json','r') as f:
            data = json.load(f)       
            entities = data['entities']
            for key in entities: #entità Q
                el = entities[key]
                for claimsId in el['claims']: #proprietà P
                    statements = el['claims'][claimsId]
                    for elem in statements: #elem è il singolo statement, statements tutti, fissata la P di sopra
                        claimsTotalNumber +=1
                        totalStatements += 1
                        if elem['rank'] == 'normal':
                            if (isAnotherPreferred(elem, statements)):
                                notAssertedCount+=1     
                            else:
                                assertedCount+=1
                        if elem['rank'] == 'preferred':
                            assertedCount+=1         
                        if elem['rank'] == 'deprecated':
                            notAssertedCount+=1
                            
                                
    except KeyError:
        print('error')
        #with open('G:/asserted3/errors/rankingsError.txt','a') as errorFile:
            #errorFile.write(file)
    except JSONDecodeError as err:
        print('error')
        #with open('G:/asserted3/errors/rankingsError.txt','a') as errorFile:
            #   errorFile.write(file)

outString = {
        'asserted': assertedCount,
        'notAsserted': notAssertedCount,
        'count':claimsTotalNumber
}
json_string = json.dumps(outString)
with open('G:/Dataset2/asserted.json','w') as output:
    output.write(json_string)