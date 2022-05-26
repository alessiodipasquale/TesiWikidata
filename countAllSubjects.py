# import required module
import os
import json
import sys
# assign directory
directory = 'G:/dumpSubject/'
count = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    with open(f, 'r') as jsonFile: 
        data = json.load(jsonFile)
        for elem in data:
           count +=1
print(count)
