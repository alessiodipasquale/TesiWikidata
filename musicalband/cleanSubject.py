# import required module
import os
import json
import sys
# assign directory
directory = '/Users/alessiodipasquale/Projects/TesiWikidata/musicalband/query.json'
    
with open(directory, 'r') as jsonFile: 
    data = json.load(jsonFile)
    print(data[0])
    outputDirectory = './cleaned.json'
    for elem in data:
        entity = str(elem['s'].replace('http://www.wikidata.org/entity/','')) + '|'
        with open(outputDirectory, 'a') as f:
            f.write(entity)
