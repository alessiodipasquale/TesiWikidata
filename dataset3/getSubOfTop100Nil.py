import json
import requests
from json.decoder import JSONDecodeError
import time
import os
#
entities = ["P2860","P1545","P2093","P31","P248","P813","P854","P698","P1476","P577","P1433","P304","P478","P1215","P1227","P433","P528","P356","P972","P50","P921","P407","P17","P932","P1932","P131","P585","P642","P2215","P106","P459","P625","P21","P3083","P6257","P6258","P6259","P580","P2671","P59","P887","P703","P735","P214","P569","P2214","P1810","P4656","P143","P2216","P5875","P27","P361","P18","P646","P582","P684","P734","P1566","P171","P225","P105","P373","P351","P2583","P1057","P279","P2888","P195","P19","P570","P1343","P1087","P2326","P276","P352","P571","P846","P69","P1412","P1082","P971","P496","P1001","P953","P1435","P227","P155","P156","P421","P281","P527","P641","P7859","P6216","P856","P1448","P7243","P108","P54"]
totalSubjects = 0
for el in entities:
   # filePath = 'G:/Dataset3/subjects/sub-%s.json' % el
    fileCountPath = 'G:/Dataset3/statementsNoValue.json'

    url = 'https://query.wikidata.org/sparql'
    query = """
    select ?statement
    {

    ?s ?p ?statement.
    ?statement a wdno:%s

    }
    """ % el
    try:
      print(el)
      r = requests.get(url, params = {'format': 'json', 'query': query})
      r.raise_for_status()
      data = r.json()
      totalSubjects += len(data['results']['bindings'])
      print(len(data['results']['bindings']))
      with open(fileCountPath, 'a') as f:
          f.write("\""+el+"\": "+str(len(data['results']['bindings']))+'\n')

      #if not os.path.exists(filePath):
      #  with open(filePath, 'w') as json_file:     
       #     json.dump(data, json_file, indent=4, separators=(',',': '))
    except NameError as err:
       # print (err)
       print("err")
    time.sleep(1)

#print(totalSubjects)