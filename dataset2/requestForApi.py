import requests
import json
import os
API_ENDPOINT = "https://www.wikidata.org/w/api.php"
i = 1
import os
directory = 'G:/Dataset2/forAPI.json'
with open(directory,'r') as file:
    line = (file.readline()).rstrip("\n")
    while line:       
        params = {
            'action': 'wbgetentities',
            'format': 'json',
            'ids': line,
            'uselang': 'en'
        }
        if not os.path.exists('G:/Dataset2/dataFromAPI/data_'+str(i)+".json"):
            r = requests.get(API_ENDPOINT, params = params)
            with open('G:/Dataset2/dataFromAPI/data_'+str(i)+".json", "w") as outfile:
                json.dump(r.json(), outfile, indent = 4)
        i+=1
        line = (file.readline()).rstrip("\n")