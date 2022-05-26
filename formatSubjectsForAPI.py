"""
def wikidata_api_data_preparation(list_of_entities):
    string = ''
    result = []

    x = 50
    w = 0
    while w < len(list_of_entities):
        while w < x:
            if w < len(list_of_entities):
                string += str(list_of_entities[w].replace('http://www.wikidata.org/entity/','')) + '|'
            w += 1
        if x == w:
            result.append(string[0:len(string)-1])
            string = ''
        x += 50
    #print('The list of entities to get from Wikidata API', result)
    return result

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
"""
with open('Q4022','r') as file:

    list_of_entities = str(file.readlines()).split('|')
    list_of_entities[0] = list_of_entities[0][2:]
    string = ''
    result = []

    x = 50
    w = 0
    while w < len(list_of_entities):
        while w < x:
            if w < len(list_of_entities):
                string += str(list_of_entities[w]+'|')
            w += 1
        if x == w:
            result.append(string[0:len(string)-1])
            string = ''
        x += 50
    with open('result','w') as file:
        for r in result:
            file.write(r+'\n')

