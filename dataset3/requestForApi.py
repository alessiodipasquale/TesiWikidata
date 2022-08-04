import requests
import json
import os
API_ENDPOINT = "https://www.wikidata.org/w/api.php"
i = 0
import os
f = 'G:\Dataset3\\forAPI.json'
with open(f,'r') as file:
    line = (file.readline()).rstrip("\n")
    while line:       
        params = {
            'action': 'wbgetentities',
            'format': 'json',
            'ids': line,
            'uselang': 'en'
        }
        if not os.path.exists('G:\Dataset3\\results\\results\data_'+str(i)+".json"):
            r = requests.get(API_ENDPOINT, params = params)
            with open('G:\Dataset3\\results\\results\data_'+str(i)+".json", "w") as outfile:
                json.dump(r.json(), outfile, indent = 4)
        else: 
            print("Skipped "+str(i))
        i+=1
        line = (file.readline()).rstrip("\n")