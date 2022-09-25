import json
from turtle import color
import matplotlib.pyplot as plt
import json
import numpy as np
import operator

with open('C:/Users/aless/Desktop/Tesi/musicalband/countBlankMusical.json','r') as file:
    data = json.load(file)
    data = sorted(data.items(), key = lambda item: item[1], reverse=True)

    
    with open('C:/Users/aless/Desktop/Tesi/musicalband/countBlankMusicalSorted.json','w') as outfile:
        outfile.write(json.dumps(data, indent = 4))