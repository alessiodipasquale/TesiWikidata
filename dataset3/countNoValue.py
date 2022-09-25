import json
from operator import contains
import requests
from json.decoder import JSONDecodeError
import time
import os

count = {
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
#
entities = ["P2860","P1545","P2093","P31","P248","P813","P854","P698","P1476","P577","P1433","P304","P478","P1215","P1227","P433","P528","P356","P972","P50","P921","P407","P17","P932","P1932","P131","P585","P642","P2215","P106","P459","P625","P21","P3083","P6257","P6258","P6259","P580","P2671","P59","P887","P703","P735","P214","P569","P2214","P1810","P4656","P143","P2216","P5875","P27","P361","P18","P646","P582","P684","P734","P1566","P171","P225","P105","P373","P351","P2583","P1057","P279","P2888","P195","P19","P570","P1343","P1087","P2326","P276","P352","P571","P846","P69","P1412","P1082","P971","P496","P1001","P953","P1435","P227","P155","P156","P421","P281","P527","P641","P7859","P6216","P856","P1448","P7243","P108","P54"]
totalSubjects = 0
#for entityType in entities:
counter = 0
for file in os.listdir("G:/Dataset3/results/results"):
    counter+=1;
    print(counter)
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
                        if(mainsnak['snaktype']=='novalue' and (claimsId in count.keys())):  
                            #print(claimsId)
                            toChange = {claimsId: count.get(claimsId)+1} 
                            count.update(toChange)
    except KeyError:
        print('key error')
        #with open('G:/asserted3/errors/rankingsError.txt','a') as errorFile:
            #errorFile.write(file)
    except JSONDecodeError as err:
        print('json error')
        
print(count) 
with open('./countBlankFINALE.json','w') as outfile:
    outfile.write(json.dumps(count, indent = 4))