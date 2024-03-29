import requests
import json
import os
API_ENDPOINT = "https://www.wikidata.org/w/api.php"
i = 0
import os
directory = 'G:/subjectForAPI/'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    with open(f,'r') as file:
        line = (file.readline()).rstrip("\n")
        while line:       
            params = {
                'action': 'wbgetentities',
                'format': 'json',
                'ids': line,
                'uselang': 'en'
            }
            if not os.path.exists('G:/results/'+filename+'_'+str(i)+".json"):
                r = requests.get(API_ENDPOINT, params = params)
                with open('G:/results/'+filename+'_'+str(i)+".json", "w") as outfile:
                    json.dump(r.json(), outfile, indent = 4)
            i+=1
            line = (file.readline()).rstrip("\n")