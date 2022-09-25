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

lista = {
    "P2860":0,
    "P1545":0,
    "P2093":0,
    "P31":0,
    "P248":0,
    "P813":0,
    "P854":0,
    "P698":0,
    "P1476":0,
    "P577":0,
    "P1433":0,
    "P304":0,
    "P478":0,
    "P1215":0,
    "P1227":0,
    "P433":0,
    "P528":0,
    "P356":0,
    "P972":0,
    "P50":0,
    "P921":0,
    "P407":0,
    "P17":0,
    "P932":0,
    "P1932":0,
    "P131":0,
    "P585":0,
    "P642":0,
    "P2215":0,
    "P106":0,
    "P459":0,
    "P625":0,
    "P21":0,
    "P3083":0,
    "P6257":0,
    "P6258":0,
    "P6259":0,
    "P580":0,
    "P2671":0,
    "P59":0,
    "P887":0,
    "P703":0,
    "P735":0,
    "P214":0,
    "P569":0,
    "P2214":0,
    "P1810":0,
    "P4656":0,
    "P143":0,
    "P2216":0,
    "P5875":0,
    "P27":0,
    "P361":0,
    "P18":0,
    "P646":0,
    "P582":0,
    "P684":0,
    "P734":0,
    "P1566":0,
    "P171":0,
    "P225":0,
    "P105":0,
    "P373":0,
    "P351":0,
    "P2583":0,
    "P1057":0,
    "P279":0,
    "P2888":0,
    "P195":0,
    "P19":0,
    "P570":0,
    "P1343":0,
    "P1087":0,
    "P2326":0,
    "P276":0,
    "P352":0,
    "P571":0,
    "P846":0,
    "P69":0,
    "P1412":0,
    "P1082":0,
    "P971":0,
    "P496":0,
    "P1001":0,
    "P953":0,
    "P1435":0,
    "P227":0,
    "P155":0,
    "P156":0,
    "P421":0,
    "P281":0,
    "P527":0,
    "P641":0,
    "P7859":0,
    "P6216":0,
    "P856":0,
    "P1448":0,
    "P7243":0,
    "P108":0,
    "P54":0
}
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
counter = 0
    #typeString=elem['type']
    #entity = str(typeString.replace('http://www.wikidata.org/entity/',''))
    #print(entity) 
    #if not os.path.exists('G:/asserted3/'+entity+'.json'):
for file in os.listdir("G:/Dataset3/results/results"):
    counter +=1
    print(counter)
    claimsTotalNumber = 0
    #if file.startswith(entity+'.json'):
    try:     
        with open('G:/Dataset3/results/results/'+file,'r') as f:
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
                        if (claimsId in lista.keys()):
                            if elem['rank'] == 'normal':
                                if (isAnotherPreferred(elem, statements)):
                                    toChange = {claimsId: lista.get(claimsId)+1} 
                                    notAssertedCount+=1    
                                    lista.update(toChange)
    
                                else:
                                    assertedCount+=1
                            if elem['rank'] == 'preferred':
                                assertedCount+=1         
                            if elem['rank'] == 'deprecated':
                                toChange = {claimsId: lista.get(claimsId)+1} 
                                notAssertedCount+=1
                                lista.update(toChange)


                            
                                
    except KeyError:
        print('error')
        #with open('G:/asserted3/errors/rankingsError.txt','a') as errorFile:
            #errorFile.write(file)
    except JSONDecodeError as err:
        print('error')
        #with open('G:/asserted3/errors/rankingsError.txt','a') as errorFile:
            #   errorFile.write(file)

#outString = {
 #       'asserted': assertedCount,
 #       'notAsserted': notAssertedCount,
 #       'count':claimsTotalNumber
#}
data = sorted(lista.items(), key = lambda item: item[1], reverse=True)

json_string = json.dumps(data)
with open('C:/Users/aless/Desktop/Tesi/dataset3/notAssertedByProperty3.json','w') as output:
    output.write(json_string)