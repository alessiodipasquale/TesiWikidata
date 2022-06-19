import json
import operator
import matplotlib.pyplot as plt
import numpy as np

with open('propertiesGroupped/merged/mergedDeprecated.json','r') as file:
    data = json.load(file)
    count = []
    entity = []
    data = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    with open('outfile.json','w') as outfile:
        outfile.write(json.dumps(data, indent = 4))
    #for el in data:
     #       entity.append(el[0])
     #       count.append(el[1])

#entity = entity[:100]
#count = count[:100]
#ind = np.arange(len(count))
#plt.figure()
#plt.bar(ind, count, tick_label = entity, width= 0.8, color='purple')
#plt.xticks(fontsize=4, rotation =90)
#plt.show()