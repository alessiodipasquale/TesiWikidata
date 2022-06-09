import os
import json
sum = 0
for file in os.listdir("G:/rankings/"):
    if file != 'errors':
        with open('G:/rankings/'+file, 'r') as f:
            data = json.load(f)
            sum += data['count']
print(sum)
        