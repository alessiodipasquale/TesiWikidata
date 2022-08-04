import json
from turtle import color
import matplotlib.pyplot as plt
import json
import numpy as np
import operator
with open('G:\Dataset3\countPath.json','r') as file:
    data = json.load(file)
    count = []
    entity = []
    data = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    print(data)

   # for key in data:
    #    if(key != 'unknown'):
     #       count.append(data[key])
      #      entity.append(key)
    
    for el in data:
        if (el[0] != 'unknown'):
            entity.append(el[0])
            count.append(el[1])
    ind = np.arange(len(count))
    plt.figure()
    plt.bar(ind, count, tick_label = entity, width= 0.8, color='purple')
    plt.xticks(fontsize=4, rotation =90)
    plt.show()