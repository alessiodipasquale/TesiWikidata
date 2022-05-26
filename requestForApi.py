from tqdm import tqdm
import requests
import json
import os
API_ENDPOINT = "https://www.wikidata.org/w/api.php"
i = 0
with open('result') as file:
   
    line = (file.readline()).rstrip("\n")
    while line:       
        params = {
            'action': 'wbgetentities',
            'format': 'json',
            'ids': line,
            'uselang': 'en'
        }
        r = requests.get(API_ENDPOINT, params = params)
        with open('results/data'+str(i)+".json", "w") as outfile:
            json.dump(r.json(), outfile, indent = 4)
        i+=1
        line = (file.readline()).rstrip("\n")