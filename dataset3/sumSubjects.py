import json
fileCountPath = 'G:/Dataset3/countPath.json'
total = 0
with open(fileCountPath, 'r') as f:
    data = json.load(f);
    for el in data:
        total += data[el]
print (total)