import json
suma = 0
with open('C:/Users/aless/Desktop/Tesi/dataset1/reasonOfDeprecation1.json','r') as f:
        #with open('C:/Users/aless/Desktop/Tesi/asserted/input/input.json','r') as f:
            data = json.load(f)
            for elem in data:
                suma+=elem[1]
            print(suma)
