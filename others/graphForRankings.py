import re
from turtle import color
import matplotlib.pyplot as plt
import json
import numpy as np
import os
import random
import operator
from tabulate import tabulate
#Deprecated valuesArray.append(data['deprecated'])
#Normal                    


directory = 'G:/rankings'
count = 0
fileNameArray = []
valuesDeprecatedArray = []
valuesNormalArray = []
valuesPreferredArray = []
valuesCountArray = []


res = []

for filename in os.listdir(directory):
    #if count < 10:
    #    rand = random.randint(1,100)
     #   if rand % 2 == 0:
            f = os.path.join(directory, filename)
            if not filename.startswith('errors'):
                with open(f,'r') as file:  
                    data = json.load(file) 
                    entity = str(filename.replace('.json',''))
                    el = {
                        "entity": str(filename.replace('.json','')),
                        "deprecated" : data['deprecated'],
                        "normal": data['normal'],
                        "preferred": data['preferred'],
                        "count": data['count']
                    }                  
                    res.append(el)
                    #entity = str(filename.replace('.json',''))
                    #fileNameArray.append(entity)
                    #valuesDeprecatedArray.append(data['deprecated'])
                    #valuesNormalArray.append(data['normal'])
                    #valuesPreferredArray.append(data['preferred'])
                    #valuesCountArray.append(data['count'])

                    count+=1
def deprecated(el):
    return el.get('deprecated')
res.sort(key=deprecated, reverse=True)
with open('sorted/deprecated.json','w') as f:
    f.write(str(res))
dep=[]
names = []
for i in range(0,100):
    dep.append(res[i]['deprecated'])
    names.append(res[i]['entity'])

ind = np.arange(len(dep))
plt.figure()
plt.bar(ind, dep, tick_label=names, width=0.9, color='red')
plt.xticks(fontsize=4, rotation =90)

def normal(el):
    return el.get('normal')
res.sort(key=normal, reverse=True)
nor=[]
names = []
with open('sorted/normal.json','w') as f:
    f.write(str(res))
for i in range(0,100):
    nor.append(res[i]['normal'])
    names.append(res[i]['entity'])
    
print(tabulate({'Entity':names, 'Normal':nor}, headers="keys", tablefmt='fancy_grid'))

ind = np.arange(len(nor))
plt.figure()
plt.bar(ind, nor, tick_label=names, width=0.9, color='orange')
plt.xticks(fontsize=4, rotation =90)


def preferred(el):
    return el.get('preferred')
res.sort(key=preferred, reverse=True)
pre=[]
names = []
with open('sorted/preferred.json','w') as f:
    f.write(str(res))
for i in range(0,100):
    pre.append(res[i]['preferred'])
    names.append(res[i]['entity'])

ind = np.arange(len(nor))
plt.figure()
plt.bar(ind, pre, tick_label=names, width=0.9, color='green')
plt.xticks(fontsize=4, rotation =90)

def count(el):
    return el.get('count')
res.sort(key=count, reverse=True)
count=[]
names = []
with open('sorted/count.json','w') as f:
    f.write(str(res))
for i in range(0,100):
    count.append(res[i]['count'])
    names.append(res[i]['entity'])

ind = np.arange(len(count))
plt.figure()
plt.bar(ind, count, tick_label=names, width=0.9, color='purple')
plt.xticks(fontsize=4, rotation =90)
plt.show()       
    
#MEDIA    
#mediaDeprecated = np.mean(valuesDeprecatedArray)       
#mediaNormal = np.mean(valuesNormalArray)       
#mediaPreferred = np.mean(valuesPreferredArray)       
#mediaCount = np.mean(valuesCountArray)  
#print('Deprecated: '+str(mediaDeprecated))
#print('Normal: '+str(mediaNormal))     
#print('Preferred: '+str(mediaPreferred))     
#print('Count: '+str(mediaCount))     
     
#plt.figure()
#plt.xticks(fontsize=5, rotation =90)
#plt.bar([1,2,3,4],[mediaDeprecated,mediaNormal,mediaPreferred,mediaCount],tick_label=['Deprecated', 'Normal', 'Preferred', 'Count'], width=0.7, color=['red','orange','green','purple'])



#PIE CHART

#sumDeprecated = np.sum(valuesDeprecatedArray)       
#sumNormal = np.sum(valuesNormalArray)       
#sumPreferred = np.sum(valuesPreferredArray)       
#plt.pie([sumDeprecated, sumNormal, sumPreferred], labels= ['Deprecated','Normal','Preferred'], colors=['red','orange','green'],startangle=90, shadow= True, radius=1.2, autopct='%1.1f%%')
#plt.legend()
    
#plt.figure()
#plt.bar(ind, getDeprecatedArray(values), tick_label ='deprecated',width= 0.7, color = 'red')

#plt.figure()
#plt.bar(ind, getNormalArray(values) ,tick_label ='normal',width= 0.7, color = 'yellow')

#plt.figure()
#plt.bar(ind, getPrefferedArray(values), tick_label ='preferred',width= 0.7, color = 'green')

  
# naming the x-axis
#plt.xlabel('Entities-Rank')
# naming the y-axis
#plt.ylabel('Values')
# plot title
#plt.title('Rankings distribution')
  
# function to show the plot
plt.show()
