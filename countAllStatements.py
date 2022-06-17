import os
import json
sumDeprecated = 0
sumNormal = 0
sumPreferred = 0
sumCount = 0
for file in os.listdir("G:/rankings/"):
    if file != 'errors':
        with open('G:/rankings/'+file, 'r') as f:
            data = json.load(f)
            sumDeprecated += data['deprecated']
            sumNormal += data['normal']
            sumPreferred += data['preferred']
            sumCount += data['count']
print('sumDeprecated: '+str(sumDeprecated))
print('sumNormal: '+str(sumNormal))
print('sumPreferred: '+str(sumPreferred))
print('sumCount: '+str(sumCount))
        