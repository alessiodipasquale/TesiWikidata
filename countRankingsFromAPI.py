from html import entities
import json
directory = './'
normalRankCount = 0
preferredRankCount = 0
deprecatedRankCount = 0
claimsTotalNumber = 0
with open("./Q123.json_3436.json",'r') as file:
    data = json.load(file)
    entities = data['entities']
    for key in entities:
        el = entities[key]
        for claimsId in el['claims']:
            statement = el['claims'][claimsId]
            for elem in statement:
                claimsTotalNumber +=1
                if elem['rank'] == 'normal':
                    normalRankCount +=1
                if elem['rank'] == 'preferred':
                    preferredRankCount +=1        
                if elem['rank'] == 'deprecated':
                    deprecatedRankCount +=1        
    print('normalRankCount: %s' % normalRankCount)
    print('preferredRankCount: %s' % preferredRankCount)
    print('deprecatedRankCount: %s' % deprecatedRankCount)
    print("Total Statements: %s" % claimsTotalNumber)