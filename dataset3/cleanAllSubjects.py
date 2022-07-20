# import required module
import os
import json
import sys
# assign directory
directory = 'G:\Dataset3\subjects'
count = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    with open(f, 'r') as jsonFile: 
        data = json.load(jsonFile)
        outputDirectory = 'G:\Dataset3\\translatedSubjects\\'+filename
        data = data['results']['bindings']
        for elem in data:
            if not elem['s']['value'].startswith('http://www.wikidata.org/entity/statement'):
                if elem['s']['value'].startswith('http://www.wikidata.org/entity/'):
                    entity = str(elem['s']['value'].replace('http://www.wikidata.org/entity/','')) + '|'
                    with open(outputDirectory, 'a') as f:
                        f.write(entity)