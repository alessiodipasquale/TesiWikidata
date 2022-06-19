import json
with open('C:/Users/aless/Desktop/Tesi/propertiesGroupped/fiumi/preferredFiumiPropertiesGroupped.json', 'r') as file1:
    data1 = json.load(file1)
    with open('C:/Users/aless/Desktop/Tesi/propertiesGroupped/preferredPropertiesGroupped.json', 'r') as file2:
        data2 = json.load(file2)
        for key in data2.keys():
            if key in data1.keys():
                toChange = {key: data2.get(key)+data1.get(key)}
                data2.update(toChange)
        for key in data1.keys():
            if key not in data2.keys():
                toChange = {key: data1.get(key)}
                data2.update(toChange)

with open('./mergedPreferred.json','w') as outfile:
    outfile.write(json.dumps(data2, indent = 4))