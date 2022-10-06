import json
import os
from json.decoder import JSONDecodeError
count = {}

for file in os.listdir("G:/fiumi/"):
    try:
        with open("G:/fiumi/"+file,'r') as f:
            data = json.load(f)               
            entities = data['entities']
            for key in entities:
                el = entities[key]
                for claimsId in el['claims']:
                    statement = el['claims'][claimsId]
                    for elem in statement:
                        prop = elem['mainsnak']['property']
                        if elem['rank']=='normal':
                            if prop not in count.keys():
                                toChange = {prop: 1}
                            else:
                                toChange = {prop: count.get(prop)+1 }
                            count.update(toChange)
                            
                        #claimsTotalNumber +=1
                        #if elem['rank'] == 'normal':
                            #   normalRankCount +=1
                        #if elem['rank'] == 'preferred':
                        #    preferredRankCount +=1        
                        #if elem['rank'] == 'deprecated':
                        # deprecatedRankCount +=1 
    except KeyError:
        a=0
    except JSONDecodeError as err:
        a=0

                        
with open('./propertiesGroupped/fiumi/normalFiumiPropertiesGroupped.json','w') as outfile:
    outfile.write(json.dumps(count, indent = 4))
