# import required module
import os
import json
import sys
# assign directory
#directory = 'G:/dumpSubject/'
directory = 'C:/Users/aless/Desktop/Tesi/first7Dataset1'
count = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    with open(f, 'r') as jsonFile: 
        data = json.load(jsonFile)
        for elem in data:
           count +=1
    print(filename+':'+ str(count))
    count = 0
