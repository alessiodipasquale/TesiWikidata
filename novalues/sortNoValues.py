import os
import json
directory = 'G:/novalues1'
res = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if filename != 'novaluesdataset1.zip':
        with open(f, 'r',  errors="ignore") as file:
            data = json.load(file)
            el = {
                "entity": filename,
                "novalues":data['novalues']
            }
            res.append(el)
        
def novalues(el):
    return el.get('novalues')
    
res.sort(key=novalues, reverse=True)
for i in range (0,10):
    print(res[i])