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
        outputDirectory = 'G:/translatedSubject/'+filename
        for elem in data:
            
            entity = str(elem['s']['value'].replace('http://www.wikidata.org/entity/','')) + '|'
            with open(outputDirectory, 'a') as f:
                f.write(entity)
